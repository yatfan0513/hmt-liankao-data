# HMT 联考招生数据 — Termux 操作指南

本教程适用于 Android 手机或平板上的 Termux。

如果第一次使用 Termux，可以完全按照下面的顺序操作。

---

# 一、安装 Termux

打开 Termux。

如果看到：

```text
$
```

说明已经进入命令行。

教程中的 `$` 不需要输入。

---

# 二、更新 Termux

输入：

```bash
pkg update && pkg upgrade
```

如果出现：

```text
Do you want to continue? [Y/n]
```

输入：

```text
y
```

然后按 Enter。

---

# 三、安装 Python

输入：

```bash
pkg install python
```

如果要求确认：

```text
y
```

然后按 Enter。

检查：

```bash
python --version
```

如果显示：

```text
Python 3.x.x
```

说明安装成功。

---

# 四、安装 Git

输入：

```bash
pkg install git
```

然后按照提示完成安装。

---

# 五、下载项目

输入：

```bash
git clone https://github.com/yatfan0513/hmt-liankao-data.git
```

下载完成后进入项目：

```bash
cd hmt-liankao-data
```

---

# 六、检查项目文件

输入：

```bash
ls
```

应该能看到：

```text
bar.js
bar.py
bar.xlsx
crawl_lzks.py
data.js
index.html
mark.js
year.js
啟動網站.bat
实测.png
readme
```

---

# 七、安装 Python 依赖

输入：

```bash
python -m pip install requests beautifulsoup4 tqdm pandas openpyxl
```

本项目主要使用：

```text
requests
beautifulsoup4
tqdm
pandas
openpyxl
```

等待安装完成。

---

# 八、第一步：修改 year.js

进入项目目录：

```bash
cd ~/hmt-liankao-data
```

使用 nano 打开：

```bash
nano year.js
```

把年份修改为当前实际年份。

例如：

```text
2027
```

保存：

```text
Ctrl + O
```

按 Enter。

退出：

```text
Ctrl + X
```

---

# 九、year.js 的作用

`year.js` 记录当前网站使用的年份。

例如：

```text
year.js = 2027
```

网站就按照 2027 年显示和处理。

同时：

```text
bar.py
```

会计算：

```text
2027 - 1 = 2026
```

所以：

```text
bar.xlsx
```

应该是 2026 年各院校分数线。

---

# 十、第二步：运行 crawl_lzks.py

运行：

```bash
python crawl_lzks.py
```

程序开始爬取招生数据。

运行期间不要随意关闭 Termux。

---

# 十一、爬虫运行时间

目前实测：

```text
约 1 分钟左右
```

实际运行时间可能不同。

影响因素包括：

- 手机网络
- 官方网站响应速度
- 官方服务器状态
- 数据量

项目中的：

```text
实测.png
```

是爬虫运行实测截图。

---

# 十二、第三步：确认 data.js

爬虫完成后会生成或更新：

```text
data.js
```

它是：

```text
crawl_lzks.py
```

获取的招生数据。

通常不需要手动修改。

---

# 十三、第四步：更新 mark.js

获得：

```text
year.js
```

所表示年份的最低分数线。

例如：

```text
year.js = 2027
```

需要获得：

```text
2027 年最低分数线
```

建议从官方渠道获得，例如：

```text
广东省教育考试院官方网站
广东省教育考试院官方微信公众号
全国联招相关官方公告
```

可以使用手机浏览器查看官方数据。

然后编辑：

```bash
nano mark.js
```

按照原文件的数据格式修改。

保存：

```text
Ctrl + O
```

Enter。

退出：

```text
Ctrl + X
```

---

# 十四、第五步：准备 bar.xlsx

需要准备：

```text
year.js - 1
```

年份的各院校分数线。

例如：

```text
year.js = 2027
```

那么：

```text
bar.xlsx = 2026 年各院校分数线
```

---

# 十五、如何制作 bar.xlsx

从官方渠道下载上一年度各院校分数线 PDF。

如果 PDF 是扫描版：

```text
官方 PDF
↓
OCR
↓
AI 整理
↓
Excel
↓
bar.xlsx
```

最终文件必须叫：

```text
bar.xlsx
```

并放在项目根目录。

---

# 十六、第六步：运行 bar.py

确认：

```text
bar.py
bar.xlsx
```

在同一个目录。

运行：

```bash
python bar.py
```

程序会读取：

```text
year.js
```

计算：

```text
year.js - 1
```

然后把 `bar.xlsx` 中的数据加入：

```text
bar.js
```

---

# 十七、bar.py 会保留往年数据

例如原来的 `bar.js` 有：

```text
2024
2025
```

现在：

```text
year.js = 2027
```

那么：

```text
bar.xlsx = 2026
```

运行：

```bash
python bar.py
```

之后应当保留：

```text
2024
2025
2026
```

不会删除以前的数据。

---

# 十八、bar.js 必须存在

即使目前没有历史分数线，也不要删除：

```text
bar.js
```

必须保留这个文件。

否则：

```text
index.html
```

可能无法正常使用。

---

# 十九、第七步：启动网站

Termux 不使用 Windows 的：

```text
啟動網站.bat
```

在 Termux 中运行：

```bash
python -m http.server 8000
```

如果看到类似：

```text
Serving HTTP on 0.0.0.0 port 8000
```

说明服务器已经启动。

---

# 二十、浏览器访问

打开 Android 浏览器。

地址栏输入：

```text
http://127.0.0.1:8000
```

按 Enter。

即可访问：

```text
index.html
```

---

# 二十一、为什么使用 127.0.0.1:8000？

直接打开：

```text
index.html
```

可能使用：

```text
file:///
```

部分浏览器会限制本地网页读取 JavaScript 文件。

因此可能出现：

```text
网页可以打开
但是没有数据
```

或者：

```text
数据加载失败
```

运行：

```bash
python -m http.server 8000
```

再访问：

```text
http://127.0.0.1:8000
```

网页就通过 HTTP 运行。

---

# 二十二、停止网站

回到 Termux。

按：

```text
Ctrl + C
```

即可停止 HTTP 服务。

---

# 二十三、以后每年更新

假设下一年需要更新。

## ① 修改 year.js

```bash
nano year.js
```

修改为实际年份。

---

## ② 运行爬虫

```bash
python crawl_lzks.py
```

---

## ③ 确认 data.js

确认：

```text
data.js
```

已经更新。

---

## ④ 更新 mark.js

从官方渠道获得当前年份最低分数线。

修改：

```bash
nano mark.js
```

---

## ⑤ 准备 bar.xlsx

计算：

```text
year.js - 1
```

获取这个年份的各院校分数线 PDF。

扫描版 PDF：

```text
PDF
↓
OCR
↓
AI
↓
Excel
↓
bar.xlsx
```

---

## ⑥ 更新 bar.js

运行：

```bash
python bar.py
```

---

## ⑦ 启动网站

```bash
python -m http.server 8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

---

# 二十四、第一次完整命令

如果刚安装好 Termux，可以按照下面执行：

```bash
pkg update && pkg upgrade
pkg install python
pkg install git
git clone https://github.com/yatfan0513/hmt-liankao-data.git
cd hmt-liankao-data
python -m pip install requests beautifulsoup4 tqdm pandas openpyxl
```

然后运行：

```bash
python crawl_lzks.py
```

修改：

```text
year.js
mark.js
```

准备：

```text
bar.xlsx
```

再运行：

```bash
python bar.py
```

最后：

```bash
python -m http.server 8000
```

浏览器打开：

```text
http://127.0.0.1:8000
```

---

# 二十五、常见问题

## 1. Python 找不到

运行：

```bash
pkg install python
```

然后：

```bash
python --version
```

---

## 2. Git 找不到

运行：

```bash
pkg install git
```

---

## 3. 找不到 crawl_lzks.py

运行：

```bash
cd ~/hmt-liankao-data
ls
```

确认存在：

```text
crawl_lzks.py
```

---

## 4. bar.py 找不到 bar.xlsx

确认：

```text
bar.py
bar.xlsx
```

在同一个目录。

---

## 5. 网页没有数据

运行：

```bash
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

---

## 6. 没有历史分数线

不要删除：

```text
bar.js
```

保留空的有效数据文件即可。

以后获得官方数据后制作：

```text
bar.xlsx
```

然后运行：

```bash
python bar.py
```
