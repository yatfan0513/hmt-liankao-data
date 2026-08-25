#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================
  2026年全国联招 - 招生院校及专业全量爬虫 (并行加速版)
  目标: https://www.eeagd.edu.cn/lzks/yxzycx/
  输出: data.js (包含 allSchools + allMajors)
=============================================================

【使用说明】
  1. 安装依赖:  pip install requests beautifulsoup4 tqdm
  2. 运行脚本:  python crawl_lzks.py
  3. 脚本自动获取全部院校、专业列表、专业详情数据，生成data.js
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import json
import time
import os
import sys
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from tqdm import tqdm
except ImportError:
    print("缺少进度条库，正在自动安装 tqdm...")
    os.system(f"{sys.executable} -m pip install tqdm -q")
    from tqdm import tqdm

# ============================================================
#  全局配置
# ============================================================
BASE_URL = "https://www.eeagd.edu.cn/lzks/yxzycx"
URL_LIST = f"{BASE_URL}/yxzycx.jsp"
URL_SCHOOL = f"{BASE_URL}/yxxx_view.jsp"
URL_MAJOR_LIST = f"{BASE_URL}/yxzy.jsp"
URL_MAJOR_DETAIL = f"{BASE_URL}/zyxx_view.jsp"

OUTPUT_FILE = "data.js"
TIMEOUT = 30
NUM_WORKERS = 15  # 并发线程数

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

PC_MAP = {"本科": "11", "预科": "19"}
JHLB_MAP = {"普通类": "00", "体育类": "30", "艺术类": "80"}
ZYKL_MAP = {"文史类": "1", "理工类": "2"}


# ============================================================
#  网络层
# ============================================================
def create_session():
    session = requests.Session()
    retry = Retry(total=2, backoff_factor=0.5,
                  status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["GET"])
    adapter = HTTPAdapter(max_retries=retry, pool_connections=20, pool_maxsize=30)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(HEADERS)
    return session


def fetch_single(session, url, referer=None, timeout=TIMEOUT):
    """单次请求，不带延迟"""
    headers = HEADERS.copy()
    if referer:
        headers["Referer"] = referer
    try:
        resp = session.get(url, headers=headers, timeout=timeout)
        resp.encoding = resp.apparent_encoding or "utf-8"
        return resp.text
    except Exception as e:
        return None


def fetch_batch(session, urls_with_ref, desc=""):
    """批量并行请求，返回结果列表(按输入顺序)"""
    results = [None] * len(urls_with_ref)
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        futures = {}
        for i, (url, ref) in enumerate(urls_with_ref):
            fut = executor.submit(fetch_single, session, url, ref)
            futures[fut] = i
        for fut in tqdm(as_completed(futures), total=len(futures), desc=desc, unit="条", ncols=100, dynamic_ncols=True):
            idx = futures[fut]
            results[idx] = fut.result()
    return results


# ============================================================
#  解析层
# ============================================================
def parse_school_list(html):
    """解析院校列表页 yxzycx.jsp"""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="tableb")
    if not table:
        return {}

    schools = {}
    total_major = 0
    total_plan = 0

    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) >= 8:
            code = cells[0]
            name = cells[1]
            if code not in schools:
                schools[code] = {"name": name, "records": []}

            record = {
                "pc": PC_MAP.get(cells[2], cells[2]),
                "pc_text": cells[2],
                "jhlb": JHLB_MAP.get(cells[3], cells[3]),
                "jhlb_text": cells[3],
                "zykl": ZYKL_MAP.get(cells[4], cells[4]),
                "zykl_text": cells[4],
                "major_count": cells[5],
                "plan_count": cells[6],
                "scope": cells[7],
            }
            schools[code]["records"].append(record)
            try: total_major += int(cells[5])
            except: pass
            try: total_plan += int(cells[6])
            except: pass

    print(f"  总记录数: {sum(len(v['records']) for v in schools.values())} 条")
    print(f"  标注专业总数: {total_major}")
    print(f"  标注招生人数: {total_plan}")
    return schools


def parse_school_detail(html):
    """解析院校详情页 yxxx_view.jsp"""
    soup = BeautifulSoup(html, "html.parser")
    info = {}
    label_map = {
        "院校代码": "schoolCode", "院校名称": "schoolName",
        "院校简介": "intro", "备注": "remark",
        "联系部门": "contact_dept", "联系人": "contact_person",
        "咨询电话": "phone", "传真": "fax",
        "招生网站": "website", "邮箱": "email",
        "院校地址": "address", "邮政编码": "zipcode",
    }
    for tr in soup.find_all("tr"):
        tds = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(tds) < 2:
            continue
        pairs = [(0, 1), (2, 3)] if len(tds) >= 4 else [(0, 1)]
        for i, v_idx in pairs:
            label = tds[i].replace(" ", "").replace(":", "").strip()
            value = tds[v_idx] if len(tds) > v_idx else ""
            key = label_map.get(label)
            if not key:
                for k, v in label_map.items():
                    if k in label or label in k:
                        key = v
                        break
            if key and key not in info:
                info[key] = value
    return info


def parse_major_list(html, yx_h, pc_text, jhlb_text, zykl_text):
    """解析专业列表页 yxzy.jsp"""
    soup = BeautifulSoup(html, "html.parser")
    majors = []
    title_match = re.search(r'招生专业数：(\d+)', html)
    total_count = int(title_match.group(1)) if title_match else None

    table = soup.find("table", class_="tableb")
    if not table:
        return majors, total_count

    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) >= 7:
            major_code = cells[2]
            major_name = cells[3]
            if major_code and major_name:
                majors.append({
                    "school_code": yx_h,
                    "school_name": cells[1],
                    "major_code": major_code,
                    "major_name": major_name,
                    "pc": pc_text,
                    "jhlb": jhlb_text,
                    "zykl": zykl_text,
                    "location": "",
                    "major_direction": "",
                    "study_duration": "",
                    "tuition": "",
                    "major_remark": "",
                })
    return majors, total_count


def parse_major_detail(html):
    """解析专业详情页 zyxx_view.jsp"""
    if not html:
        return {}
    soup = BeautifulSoup(html, "html.parser")
    info = {}
    for tr in soup.find_all("tr"):
        tds = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(tds) >= 2:
            label = tds[0].replace(" ", "").replace(":", "").strip()
            value = tds[1].strip()
            if label == "专业方向":
                info["major_direction"] = value
            elif label == "学制":
                info["study_duration"] = value.replace("年", "")
            elif label == "备注":
                info["major_remark"] = value
    return info


def extract_location(address):
    """从地址中提取省市"""
    if not address:
        return ""
    match = re.match(
        r'(北京|上海|天津|重庆|广东|江苏|浙江|山东|湖北|湖南|四川|陕西|福建|'
        r'河南|河北|辽宁|吉林|黑龙江|安徽|江西|云南|贵州|广西|甘肃|'
        r'青海|宁夏|新疆|内蒙古|西藏|海南|山西|台湾|香港|澳门)',
        address
    )
    if match:
        return match.group(1)
    return address.split()[0] if " " in address else address


def derive_tags(records):
    """从records中推导tags"""
    tags = set()
    for r in records:
        if r["pc_text"]: tags.add(r["pc_text"])
        if r["jhlb_text"]: tags.add(r["jhlb_text"])
        if r["zykl_text"]: tags.add(r["zykl_text"])
    return sorted(tags)


# ============================================================
#  主流程
# ============================================================
def main():
    print("=" * 60)
    print("  2026年全国联招 招生院校及专业全量爬虫 (并行加速版)")
    print("  目标: https://www.eeagd.edu.cn/lzks/yxzycx/")
    print("  输出: data.js (allSchools + allMajors)")
    print("=" * 60)
    print()

    session = create_session()

    # --- 步骤1: 获取院校列表 ---
    print("【步骤1】获取院校列表...")
    html = fetch_single(session, URL_LIST)
    if not html:
        print("ERROR: 无法获取院校列表页!")
        sys.exit(1)

    schools_data = parse_school_list(html)
    school_count = len(schools_data)
    print(f"  去重院校: {school_count} 所")
    print()

    # --- 步骤2: 并行获取院校详情 ---
    print("【步骤2】并行获取院校详情...")
    school_urls = [(f"{URL_SCHOOL}?yx_h={code}", URL_LIST) for code in schools_data.keys()]
    school_htmls = fetch_batch(session, school_urls, desc="  院校详情")

    school_details = {}
    for code, h in zip(schools_data.keys(), school_htmls):
        if h:
            info = parse_school_detail(h)
            info["schoolCode"] = code
            school_details[code] = info
    print(f"  成功: {len(school_details)} 所")
    print()

    # --- 步骤3: 并行获取专业列表 ---
    print("【步骤3】并行获取专业列表...")
    major_list_tasks = []
    for code in sorted(schools_data.keys()):
        for record in schools_data[code]["records"]:
            pc_code = record["pc"]
            if pc_code == "19":  # 预科跳过
                continue
            url = (f"{URL_MAJOR_LIST}?yx_h={code}&pc_h={record['pc']}&"
                   f"jhlb_h={record['jhlb']}&zykl_h={record['zykl']}")
            major_list_tasks.append((url, code, record["pc_text"], record["jhlb_text"], record["zykl_text"]))

    print(f"  待请求专业列表页: {len(major_list_tasks)} 个")
    major_list_htmls = fetch_batch(session, [(t[0], URL_LIST) for t in major_list_tasks], desc="  专业列表")

    all_majors = []
    total_list_count = 0
    for h, task in zip(major_list_htmls, major_list_tasks):
        if h:
            url, code, pc_text, jhlb_text, zykl_text = task
            majors, list_count = parse_major_list(h, code, pc_text, jhlb_text, zykl_text)
            all_majors.extend(majors)
            total_list_count += list_count if list_count else len(majors)

    print(f"  成功: {len(all_majors)} 条专业记录")
    print(f"  列表页标注总数: {total_list_count}")
    print()

    # --- 步骤4: 并行获取专业详情 ---
    print("【步骤4】并行获取专业详情(专业方向、学制、备注)...")

    detail_tasks = []
    for i, m in enumerate(all_majors):
        url = f"{URL_MAJOR_DETAIL}?zy_h={m['major_code']}&yx_h={m['school_code']}"
        detail_tasks.append((url, i))

    detail_htmls = fetch_batch(session, [(t[0], None) for t in detail_tasks], desc="  专业详情")

    for h, task in zip(detail_htmls, detail_tasks):
        idx = task[1]
        detail = parse_major_detail(h)
        all_majors[idx].update(detail)

    # 填充location
    for m in all_majors:
        addr = school_details.get(m["school_code"], {}).get("address", "")
        m["location"] = extract_location(addr)

    print(f"  详情获取完成")
    print()

    # --- 步骤5: 构建最终数据 ---
    print("【步骤5】构建数据并生成data.js...")

    all_schools = []
    total_major = 0
    total_plan = 0

    for code in sorted(schools_data.keys()):
        data = schools_data[code]
        detail = school_details.get(code, {})
        records = data["records"]
        address = detail.get("address", "")
        location = extract_location(address)
        tags = derive_tags(records)

        for r in records:
            try: total_major += int(r["major_count"])
            except: pass
            try: total_plan += int(r["plan_count"])
            except: pass

        school = {
            "code": code,
            "name": data["name"],
            "location": location,
            "intro": detail.get("intro", ""),
            "remark": detail.get("remark", ""),
            "contact_dept": detail.get("contact_dept", ""),
            "contact_person": detail.get("contact_person", ""),
            "phone": detail.get("phone", ""),
            "fax": detail.get("fax", ""),
            "website": detail.get("website", ""),
            "email": detail.get("email", ""),
            "address": address,
            "zipcode": detail.get("zipcode", ""),
            "records": records,
            "tags": tags,
            "history_scores_2025": {},
        }
        all_schools.append(school)

    # --- 步骤6: 输出data.js ---
    print("\n【步骤6】写入data.js...")

    js_content = f"""\
// ============================================================
// 2026年全国联招 - 招生院校及专业数据
// 数据来源: https://www.eeagd.edu.cn/lzks/
// 爬取时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
// 院校总数: {school_count}
// 专业总数(allMajors): {len(all_majors)}
// 招生人数: {total_plan}
// ============================================================

var allSchools = {json.dumps(all_schools, ensure_ascii=False, indent=2)};

var allMajors = {json.dumps(all_majors, ensure_ascii=False, indent=2)};

var stats = {{
    totalSchools: {school_count},
    totalMajors: {len(all_majors)},
    totalPlans: {total_plan},
}};

function getSchools() {{ return allSchools; }}
function getMajors() {{ return allMajors; }}
function getStats() {{ return stats; }}

function searchSchools(keyword) {{
    var kw = keyword.toLowerCase();
    return allSchools.filter(function(s) {{
        return (s.name || '').toLowerCase().indexOf(kw) !== -1 ||
               (s.code || '').toLowerCase().indexOf(kw) !== -1;
    }});
}}

function filterSchools(opts) {{
    return allSchools.filter(function(s) {{
        if (opts.batch) {{
            var found = false;
            s.records.forEach(function(r) {{ if (r.pc_text === opts.batch) found = true; }});
            if (!found) return false;
        }}
        if (opts.planType) {{
            var found = false;
            s.records.forEach(function(r) {{ if (r.jhlb_text === opts.planType) found = true; }});
            if (!found) return false;
        }}
        if (opts.subjectType) {{
            var found = false;
            s.records.forEach(function(r) {{ if (r.zykl_text === opts.subjectType) found = true; }});
            if (!found) return false;
        }}
        if (opts.province && (s.location || '').indexOf(opts.province) === -1) return false;
        if (opts.tag && s.tags.indexOf(opts.tag) === -1) return false;
        return true;
    }});
}}

function getSchoolByCode(code) {{
    return allSchools.find(function(s) {{ return s.code === code; }});
}}

function searchMajors(keyword) {{
    var kw = keyword.toLowerCase();
    return allMajors.filter(function(m) {{
        return (m.major_name || '').toLowerCase().indexOf(kw) !== -1 ||
               (m.school_name || '').toLowerCase().indexOf(kw) !== -1 ||
               (m.major_code || '').toLowerCase().indexOf(kw) !== -1;
    }});
}}

function filterMajors(opts) {{
    return allMajors.filter(function(m) {{
        if (opts.batch && m.pc !== opts.batch) return false;
        if (opts.planType && m.jhlb !== opts.planType) return false;
        if (opts.subjectType && m.zykl !== opts.subjectType) return false;
        if (opts.province && m.location.indexOf(opts.province) === -1) return false;
        if (opts.keyword) {{
            var kw = opts.keyword.toLowerCase();
            if (m.major_name.toLowerCase().indexOf(kw) === -1 &&
                m.school_name.toLowerCase().indexOf(kw) === -1) return false;
        }}
        return true;
    }});
}}
"""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)

    size_kb = os.path.getsize(OUTPUT_FILE) / 1024
    print(f"\n{'=' * 60}")
    print(f"  爬取完成!")
    print(f"  院校: {school_count} 所")
    print(f"  专业记录(allMajors): {len(all_majors)} 条")
    print(f"  招生人数: {total_plan} 人")
    print(f"  文件: {OUTPUT_FILE} ({size_kb:.1f} KB)")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
