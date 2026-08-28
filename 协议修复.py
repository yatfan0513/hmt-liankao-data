import socket
import re
import os
import sys
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# 尝试引入 tqdm，如果没有则使用简单的文本进度
try:
    from tqdm import tqdm
    USE_TQDM = True
except ImportError:
    USE_TQDM = False
    def tqdm(iterable, **kwargs):
        return iterable

# 1. 探测协议函数
def check_protocol(domain):
    """通过 TCP 端口探测判断协议"""
    # 先检查 443 (HTTPS)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((domain, 443))
        sock.close()
        if result == 0:
            return 'https://'
    except:
        pass

    # 再检查 80 (HTTP)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((domain, 80))
        sock.close()
        if result == 0:
            return 'http://'
    except:
        pass

    # 都打不开默认 https
    return 'https://'

# 2. 清理网址并判断协议
def clean_and_fix_url(url_str, protocol_cache):
    if not isinstance(url_str, str) or not url_str.strip():
        return url_str, None

    original_url = url_str
    
    # 去掉无关中文和多余空格 (修复了 \s 警告)
    url_str = re.sub(r'[，。！？；：""''【】（）\s]+', '', url_str)
    
    # 提取纯 URL (支持多级域名如 .edu.cn)
    match = re.search(r'(https?://[^\s<>"\']+|www\.[^\s<>"\']+|[a-zA-Z0-9][-a-zA-Z0-9]*(?:\.[a-zA-Z0-9][-a-zA-Z0-9]*)+\.[a-zA-Z]{2,}(?:/[^\s<>"\']*)?)', url_str)
    if not match:
        return url_str, None
        
    pure_url = match.group(1)
    
    # 优先选择招生网
    if 'zsb' in pure_url or 'admission' in pure_url or 'zsxxw' in pure_url:
        chosen_url = pure_url
    else:
        chosen_url = pure_url

    # 判断是否需要修复协议
    if chosen_url.startswith('http://') or chosen_url.startswith('https://'):
        return chosen_url, None  # 已有协议，不修改
    
    # 缺少协议，进行探测
    domain_match = re.search(r'(www\.[^\s<>"\']+|[a-zA-Z0-9][-a-zA-Z0-9]*(?:\.[a-zA-Z0-9][-a-zA-Z0-9]*)+\.[a-zA-Z]{2,})', chosen_url)
    domain = domain_match.group(1) if domain_match else chosen_url.split('/')[0]
    
    if domain in protocol_cache:
        protocol = protocol_cache[domain]
    else:
        protocol = check_protocol(domain)
        protocol_cache[domain] = protocol
        
    new_url = protocol + chosen_url
    return new_url, f"缺少协议，自动补全为 {protocol}"

# 3. 精确提取 allSchools 数组 (括号计数法)
def extract_all_schools(js_content):
    start_marker = 'var allSchools = ['
    start_idx = js_content.find(start_marker)
    if start_idx == -1:
        raise ValueError("data.js 中未找到 'var allSchools = ['")
    
    bracket_start = js_content.index('[', start_idx)
    depth = 0
    in_string = False
    escape_next = False
    end_idx = -1
    
    for i in range(bracket_start, len(js_content)):
        char = js_content[i]
        if escape_next:
            escape_next = False
            continue
        if char == '\\' and in_string:
            escape_next = True
            continue
        if char == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            if depth == 0:
                end_idx = i
                break
                
    if end_idx == -1:
        raise ValueError("无法找到 allSchools 数组的结束括号")
        
    array_str = js_content[bracket_start : end_idx + 1]
    return json.loads(array_str), bracket_start, end_idx + 1

# 4. 主程序
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 多文件名兼容
    possible_names = ['data（爬虫数据）.js', 'data_cleaned.js', 'data.js']
    data_js_path = None
    for name in possible_names:
        p = os.path.join(script_dir, name)
        if os.path.exists(p):
            data_js_path = p
            break
            
    if not data_js_path:
        print("错误: 未找到 data.js 或 data_cleaned.js 或 data（爬虫数据）.js")
        sys.exit(1)
        
    output_js_path = os.path.join(script_dir, 'data_协议修复.js')
    log_path = os.path.join(script_dir, '已修改协议.txt')
    
    print(f"读取文件: {data_js_path}")
    with open(data_js_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    schools, start, end = extract_all_schools(js_content)
    print(f"共提取到 {len(schools)} 所院校")
    
    # 获取所有需要探测的域名 (去重)
    domains_to_check = set()
    for school in schools:
        url = school.get('website', '')
        if isinstance(url, str) and url and not url.startswith('http://') and not url.startswith('https://'):
            match = re.search(r'(www\.[^\s<>"\']+|[a-zA-Z0-9][-a-zA-Z0-9]*(?:\.[a-zA-Z0-9][-a-zA-Z0-9]*)+\.[a-zA-Z]{2,})', url)
            if match:
                domains_to_check.add(match.group(1))
                
    # 并发探测协议，带进度条
    protocol_cache = {}
    if domains_to_check:
        print(f"开始探测 {len(domains_to_check)} 个域名的协议...")
        with ThreadPoolExecutor(max_workers=20) as executor:
            future_to_domain = {executor.submit(check_protocol, domain): domain for domain in domains_to_check}
            for future in tqdm(as_completed(future_to_domain), total=len(future_to_domain), desc="探测协议", ncols=80):
                domain = future_to_domain[future]
                protocol_cache[domain] = future.result()
                
    # 修复网址
    modified_count = 0
    modify_log = []
    
    print("正在修复网址...")
    for school in tqdm(schools, desc="修复网址", ncols=80):
        url = school.get('website', '')
        if not isinstance(url, str) or not url.strip():
            continue
            
        new_url, reason = clean_and_fix_url(url, protocol_cache)
            
        if new_url != url:
            school['website'] = new_url
            modified_count += 1
            modify_log.append(f"{school.get('code', 'N/A')}\t{school.get('name', 'N/A')}\t{url}\t{new_url}")
            
    # 写回文件
    new_array_str = json.dumps(schools, ensure_ascii=False, indent=2)
    new_js_content = js_content[:start] + new_array_str + js_content[end:]
    
    with open(output_js_path, 'w', encoding='utf-8') as f:
        f.write(new_js_content)
        
    # 写入日志
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("院校代码\t院校名称\t修改前网址\t修改后网址\n")
        for log in modify_log:
            f.write(log + "\n")
        
    print(f"\n✓ 修复完成! 共修改 {modified_count} 个网址")
    print(f"✓ 结果已保存至: {output_js_path}")
    print(f"✓ 修改记录已保存至: {log_path}")

if __name__ == '__main__':
    main()