# HMT 联考招生数据 — Windows 操作指南

本教程适合第一次使用 Python、CMD 和本地网页的 Windows 用户。

按照下面的顺序操作即可。

---

## 一、准备项目文件夹

先将整个项目下载到电脑。

例如放在：

```text
C:\Users\ABC\Documents\hmt-liankao-data
```

这里的 `ABC` 只是示例，请根据电脑实际情况替换。

项目文件夹中应有：

```text
hmt-liankao-data/
│
├── readme/
│   ├── README-Termux.md
│   └── README-Windows.md
│
├── bar.js
├── bar.py
├── bar.xlsx
├── crawl_lzks.py
├── data.js
├── index.html
├── mark.js
├── year.js
├── 啟動網站.bat
└── 实测.png
```

---

## 二、安装 Python

打开浏览器，进入：

```text
https://www.python.org/
```

下载适用于 Windows 的 Python。

安装时，如果看到：

```text
Add Python to PATH
```

请勾选。

然后完成安装。

---

## 三、检查 Python 是否安装成功

按：

```text
Win + R
```

输入：

```text
cmd
```

按 Enter。

出现黑色窗口后输入：

```cmd
python --version
```

如果看到类似：

```text
Python 3.13.7
```

说明 Python 已经安装成功。

---

## 四、安装依赖

在 CMD 输入：

```cmd
python -m pip install requests beautifulsoup4 tqdm pandas openpyxl
```

等待安装完成。

本项目使用的主要 Python 库：

```text
requests
beautifulsoup4
tqdm
pandas
openpyxl
```

以后如果已经安装过这些依赖，一般不需要重复安装。

---

## 五、进入项目文件夹

假设项目位置：

```text
C:\Users\ABC\Documents\hmt-liankao-data
```

在 CMD 输入：

```cmd
cd C:\Users\ABC\Documents\hmt-liankao-data
```

然后按 Enter。

输入：

```cmd
dir
```

如果能够看到：

```text
crawl_lzks.py
index.html
year.js
mark.js
bar.py
bar.js
```

说明进入了正确的文件夹。

---

# 六、第一步：修改 year.js

找到：

```text
year.js
```

右键：

```text
打开方式 → 记事本
```

按照当前实际年份修改。

例如当前年份是：

```text
2027
```

就设置为：

```text
2027
```

保存文件。

---

# 七、第二步：运行爬虫

回到 CMD。

确认当前目录是项目目录：

```text
C:\Users\ABC\Documents\hmt-liankao-data
```

输入：

```cmd
python crawl_lzks.py
```

按 Enter。

程序开始爬取招生数据。

---

## 八、爬虫运行时间

目前实测：

```text
约 1 分钟左右
```

实际时间不固定。

可能受到：

- 网络速度
- 官方网站响应速度
- 官方服务器状态
- 数据量

等因素影响。

项目中的：

```text
实测.png
```

是爬虫运行的实测截图。

---

# 九、第三步：确认 data.js

爬虫完成后，会生成或更新：

```text
data.js
```

这是：

```text
crawl_lzks.py
```

获取的招生数据。

一般不要手动修改 `data.js`。

---

# 十、第四步：更新 mark.js

现在需要获得：

```text
year.js
```

所表示年份的最低分数线。

例如：

```text
year.js = 2027
```

就需要获得：

```text
2027 年最低分数线
```

可以从官方渠道获取，例如：

```text
广东省教育考试院官方网站
广东省教育考试院官方微信公众号
全国联招相关官方公告
```

获得数据后，打开：

```text
mark.js
```

按照原文件格式修改并保存。

---

# 十一、第五步：准备 bar.xlsx

现在需要准备上一年度各院校分数线。

计算：

```text
year.js - 1
```

例如：

```text
year.js = 2027
```

那么：

```text
2027 - 1 = 2026
```

因此：

```text
bar.xlsx
```

应当保存：

```text
2026 年各院校分数线
```

---

# 十二、获取 bar.xlsx

从官方渠道下载上一年度各院校分数线 PDF。

如果下载到的是扫描版 PDF，可以：

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

最后将 Excel 文件命名为：

```text
bar.xlsx
```

并放在项目根目录。

也就是：

```text
bar.py
bar.xlsx
```

必须位于同一个文件夹。

---

# 十三、第六步：运行 bar.py

回到 CMD。

确认：

```text
bar.py
bar.xlsx
year.js
bar.js
```

都在项目目录。

输入：

```cmd
python bar.py
```

按 Enter。

程序会读取：

```text
year.js
```

然后计算：

```text
year.js - 1
```

再把 `bar.xlsx` 中的数据加入：

```text
bar.js
```

---

# 十四、bar.py 会保留历史数据

例如原来的：

```text
bar.js
```

已经有：

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

```cmd
python bar.py
```

应该保留：

```text
2024
2025
2026
```

不会删除以前的数据。

---

# 十五、bar.js 不要删除

即使暂时没有历史分数线，也必须保留：

```text
bar.js
```

否则 `index.html` 可能无法正常使用。

---

# 十六、第七步：启动网站

最简单的方法：

直接双击：

```text
啟動網站.bat
```

它会帮助启动本地网站。

---

# 十七、如果不使用啟動網站.bat

也可以自己启动。

CMD 输入：

```cmd
python -m http.server 8000
```

然后打开浏览器。

输入：

```text
http://127.0.0.1:8000
```

按 Enter。

即可访问网站。

---

# 十八、为什么需要 127.0.0.1:8000？

直接双击：

```text
index.html
```

浏览器会使用：

```text
file:///
```

某些浏览器会限制本地 HTML 读取 JavaScript 文件。

因此可能出现：

```text
网页可以打开
但是没有数据
```

或者：

```text
数据加载失败
```

这时候使用：

```cmd
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

网页就会通过 HTTP 运行。

---

# 十九、每年更新一次的完整流程

以后更新新一年数据时：

### ① 修改年份

打开：

```text
year.js
```

修改为实际年份。

### ② 运行爬虫

```cmd
python crawl_lzks.py
```

### ③ 更新招生数据

确认：

```text
data.js
```

已经更新。

### ④ 获取当前年份最低分数线

从官方渠道获取数据。

修改：

```text
mark.js
```

### ⑤ 获取上一年度院校分数线

下载官方 PDF。

扫描版 PDF 可以通过 OCR / AI 整理成：

```text
bar.xlsx
```

### ⑥ 更新历史分数线

运行：

```cmd
python bar.py
```

### ⑦ 启动网站

双击：

```text
啟動網站.bat
```

或者：

```cmd
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

---

# 二十、最常用的命令

安装依赖：

```cmd
python -m pip install requests beautifulsoup4 tqdm pandas openpyxl
```

运行爬虫：

```cmd
python crawl_lzks.py
```

更新历史分数线：

```cmd
python bar.py
```

启动网站：

```cmd
python -m http.server 8000
```

网站地址：

```text
http://127.0.0.1:8000
```

---

# 二十一、常见问题

## 1. 输入 python 后提示找不到

重新安装 Python，并确认安装时勾选：

```text
Add Python to PATH
```

然后关闭 CMD，再重新打开。

---

## 2. pip 安装失败

先检查：

```cmd
python --version
```

然后再次执行：

```cmd
python -m pip install requests beautifulsoup4 tqdm pandas openpyxl
```

---

## 3. 找不到 crawl_lzks.py

输入：

```cmd
dir
```

确认当前文件夹是否存在：

```text
crawl_lzks.py
```

如果没有，使用 `cd` 进入正确的项目目录。

---

## 4. bar.py 找不到 bar.xlsx

确认：

```text
bar.py
bar.xlsx
```

位于同一个项目目录。

---

## 5. 网页打开但没有数据

运行：

```cmd
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

保持文件存在即可。

以后获得官方历史数据后，再制作：

```text
bar.xlsx
```

并运行：

```cmd
python bar.py
```
