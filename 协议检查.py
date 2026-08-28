# -*- coding: utf-8 -*-
"""
检测 data.js 中哪些院校的 website 字段缺少 https:// 或 http:// 前缀
输出结果到 txt 文件
"""
import re
import os

# 配置路径
data_js_path = 'data.js'          # data.js 文件路径
output_txt_path = '缺少协议前缀的院校.txt'  # 输出文件路径

# 读取 data.js
with open(data_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 用正则提取每个院校的 code, name, website
pattern = r'"code"\s*:\s*"([^"]*)"[\s\S]*?"name"\s*:\s*"([^"]*)"[\s\S]*?"website"\s*:\s*"([^"]*)"'
matches = re.findall(pattern, content)

print(f"总共解析到 {len(matches)} 所院校")

# 筛选缺少 https:// 或 http:// 前缀的院校
missing_protocol = []
for code, name, website in matches:
    website_stripped = website.strip()
    if not (website_stripped.startswith('https://') or website_stripped.startswith('http://')):
        missing_protocol.append((code, name, website_stripped))

print(f"缺少 http/https 前缀的院校: {len(missing_protocol)} 所")

# 输出到 txt 文件
os.makedirs(os.path.dirname(output_txt_path) if os.path.dirname(output_txt_path) else '.', exist_ok=True)

with open(output_txt_path, 'w', encoding='utf-8') as f:
    f.write(f"data.js 中缺少 https:// 或 http:// 前缀的院校\n")
    f.write(f"检测时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}\n")
    f.write(f"总计: {len(missing_protocol)} 所\n")
    f.write("=" * 80 + "\n\n")
    for i, (code, name, website) in enumerate(missing_protocol, 1):
        f.write(f"{i}. 院校编码: {code}\n")
        f.write(f"   院校名称: {name}\n")
        f.write(f"   data.js 上的网站: {website}\n")
        f.write("-" * 40 + "\n")

print(f"\n结果已保存至: {output_txt_path}")
