#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bar.py - 读取 bar.xlsx 中的录取分数线数据，写入 bar.js 文件
         如果 bar.js 不存在，则自动创建空白的 bar.js
         自动从 year.js 读取当前年份，使用 当前年份-1 作为分数线年份
         多年份支持：新数据追加到 bar.js 中，不删除旧年份数据

运行方式: python bar.py
运行目录: 必须与 data.js、bar.js、bar.xlsx 和 year.js 在同一目录下
"""

import pandas as pd
import json
import re
import os
import sys

# 获取脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 文件路径
data_js_path = os.path.join(SCRIPT_DIR, 'data.js')
bar_js_path = os.path.join(SCRIPT_DIR, 'bar.js')
bar_xlsx_path = os.path.join(SCRIPT_DIR, 'bar.xlsx')
year_js_path = os.path.join(SCRIPT_DIR, 'year.js')

print(f"数据目录: {SCRIPT_DIR}")
print(f"data.js 路径: {data_js_path}")
print(f"bar.js 路径: {bar_js_path}")
print(f"bar.xlsx 路径: {bar_xlsx_path}")
print(f"year.js 路径: {year_js_path}")

# 检查文件是否存在
if not os.path.exists(data_js_path):
    print(f"错误: 找不到 data.js 文件: {data_js_path}")
    sys.exit(1)
# 如果 bar.js 不存在，则创建空白的 bar.js
if not os.path.exists(bar_js_path):
    print(f"bar.js 不存在，将创建新的空白 bar.js")
    with open(bar_js_path, 'w', encoding='utf-8') as f:
        f.write('var historyScoresData = {};\n')

    print(f"✓ 已创建: {bar_js_path}")
if not os.path.exists(bar_xlsx_path):
    print(f"错误: 找不到 bar.xlsx 文件: {bar_xlsx_path}")
    sys.exit(1)
if not os.path.exists(year_js_path):
    print(f"错误: 找不到 year.js 文件: {year_js_path}")
    sys.exit(1)

# ============================================
# 0. 读取 year.js 获取当前年份
# ============================================
with open(year_js_path, 'r', encoding='utf-8') as f:
    year_js = f.read()

year_match = re.search(r'currentYear\s*=\s*["\'](\d{4})["\']', year_js)
if not year_match:
    print("错误: 无法从 year.js 中提取 currentYear")
    sys.exit(1)

current_year = int(year_match.group(1))
score_year = str(current_year - 1)  # 分数线年份 = 当前年份 - 1
print(f"\nyear.js 中 currentYear = {current_year}，分数线年份 = {score_year}")

# ============================================
# 1. 读取 bar.js 中已有的分数线数据（多年份）
# ============================================
with open(bar_js_path, 'r', encoding='utf-8') as f:
    bar_js = f.read()

# 提取 historyScoresData 对象
bar_match = re.search(r'var historyScoresData\s*=\s*(\{.*?\});', bar_js, re.DOTALL)
if not bar_match:
    print("警告: bar.js 中没有找到 historyScoresData，将使用空数据")
    history_scores_data = {}
else:
    bar_json_str = bar_match.group(1)
    history_scores_data = json.loads(bar_json_str)
print(f"bar.js 中已有 {len(history_scores_data)} 所院校的分数线数据")

# ============================================
# 2. 读取 data.js 获取院校名称列表
# ============================================
with open(data_js_path, 'r', encoding='utf-8') as f:
    data_js = f.read()

# 提取 allSchools 数组的 JSON 部分
match = re.search(r'var allSchools\s*=\s*(\[.*?\]);\s*(var allMajors)?', data_js, re.DOTALL)
if not match:
    print("错误: 无法从 data.js 中提取 allSchools 数组")
    sys.exit(1)

json_str = match.group(1)
all_schools = json.loads(json_str)
print(f"读取到 {len(all_schools)} 所院校")

# 构建名称到院校数据的映射
name_to_school = {}
for s in all_schools:
    name_to_school[s['name']] = s

# ============================================
# 3. 读取 bar.xlsx 中的分数线数据
# ============================================
df_sheets = pd.read_excel(bar_xlsx_path, sheet_name=None)

# Sheet名称到 history_scores 键名的映射
sheet_key_map = {
    '本科普通类理工类': '普通类理工',
    '本科普通类文史类': '普通类文史',
    '本科艺术类理工类': '艺术类理工',
    '本科艺术类文史类': '艺术类文史',
    '本科体育类理工类': '体育类理工',
    '本科体育类文史类': '体育类文史',
}

# 存储本次从 bar.xlsx 读取到的分数线数据
score_data = {}

for sheet_name, df in df_sheets.items():
    if sheet_name == '预科批次':
        for _, row in df.iterrows():
            school_name = str(row['院校名称']).strip()
            if school_name not in score_data:
                score_data[school_name] = {}

            # 文史类
            wen_count = row.get('文史类录取人数')
            wen_score = row.get('文史类最低分')
            wen_rank = row.get('文史类最低排位')
            if not (pd.isna(wen_count) or pd.isna(wen_score) or pd.isna(wen_rank)):
                score_data[school_name]['预科文史'] = {
                    'count': str(int(wen_count)) if not pd.isna(wen_count) else '',
                    'score': str(int(wen_score)) if not pd.isna(wen_score) else '',
                    'rank': str(int(wen_rank)) if not pd.isna(wen_rank) else ''
                }

            # 理工类
            li_count = row.get('理工类录取人数')
            li_score = row.get('理工类最低分')
            li_rank = row.get('理工类最低排位')
            if not (pd.isna(li_count) or pd.isna(li_score) or pd.isna(li_rank)):
                score_data[school_name]['预科理工'] = {
                    'count': str(int(li_count)) if not pd.isna(li_count) else '',
                    'score': str(int(li_score)) if not pd.isna(li_score) else '',
                    'rank': str(int(li_rank)) if not pd.isna(li_rank) else ''
                }
        continue

    if sheet_name not in sheet_key_map:
        continue

    key = sheet_key_map[sheet_name]

    for _, row in df.iterrows():
        school_name = str(row['院校名称']).strip()
        if school_name not in score_data:
            score_data[school_name] = {}

        count_val = row.get('录取人数')
        score_val = row.get('录取最低分')
        rank_val = row.get('录取最低排位')

        if not (pd.isna(count_val) or pd.isna(score_val) or pd.isna(rank_val)):
            score_data[school_name][key] = {
                'count': str(int(count_val)) if not pd.isna(count_val) else '',
                'score': str(int(score_val)) if not pd.isna(score_val) else '',
                'rank': str(int(rank_val)) if not pd.isna(rank_val) else ''
            }

print(f"\nbar.xlsx 中共有 {len(score_data)} 所院校的分数线数据")

# ============================================
# 4. 将分数线数据合并到 history_scores_data 中（多年份支持）
# ============================================
filled_count = 0
not_found = []

for school in all_schools:
    name = school['name']

    if name in score_data:
        # 将当前年份的数据合并到 history_scores_data 中
        # 如果该年份已有数据，则覆盖；否则新增
        history_scores_data[name] = history_scores_data.get(name, {})
        history_scores_data[name][score_year] = score_data[name]
        filled_count += 1
    else:
        not_found.append(name)

print(f"\n填充结果:")
print(f"  成功填充 ({score_year}年): {filled_count} 所院校")
print(f"  未找到分数线数据: {len(not_found)} 所院校")
if not_found:
    print(f"  未匹配的院校: {not_found[:20]}")

# 按年份统计
year_counts = {}
for name, years in history_scores_data.items():
    for y in years:
        year_counts[y] = year_counts.get(y, 0) + 1

for y in sorted(year_counts.keys()):
    print(f"  {y}年: {year_counts[y]} 所院校")

# 统计各分类的填充情况
for key in ['普通类文史', '普通类理工', '艺术类文史', '艺术类理工', '体育类文史', '体育类理工', '预科文史', '预科理工']:
    count = sum(1 for name, years in history_scores_data.items() if key in years.get(score_year, {}))
    if count > 0:
        print(f"  {score_year}年 - {key}: {count} 所")

# ============================================
# 5. 写回 bar.js
# ============================================
new_bar_json = json.dumps(history_scores_data, ensure_ascii=False, indent=2)

# 替换原始的 historyScoresData 对象部分
new_bar_js = re.sub(
    r'(var historyScoresData\s*=\s*)\{.*?\}(;)',
    lambda m: m.group(1) + new_bar_json + m.group(2),
    bar_js,
    flags=re.DOTALL
)

# 写回文件
with open(bar_js_path, 'w', encoding='utf-8') as f:
    f.write(new_bar_js)

print(f"\n✓ bar.js 已更新，共填充 {filled_count} 所院校的 {score_year} 年历史分数线数据")
print(f"✓ 文件已保存至: {bar_js_path}")
