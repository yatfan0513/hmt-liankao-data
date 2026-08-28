# HMT 联考招生数据

港澳台联考招生数据爬虫与本地查询网站。

本项目用于获取港澳台联考相关招生信息，并生成可直接在浏览器中使用的本地查询页面。

> 招生政策、招生计划、最低分数线等信息可能随年份变化，请以官方公布的信息为准。

## 一、项目结构

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

## 二、每个文件的作用

### `crawl_lzks.py`

招生数据爬虫。

运行后从官方网站获取院校、专业等信息，并生成：

```text
data.js
```

运行：

```bash
python crawl_lzks.py
```

### `data.js`

`crawl_lzks.py` 获取的数据。

`index.html` 会读取这个文件。

通常不需要手动修改。

### `index.html`

项目实际使用的查询网页。

网页会读取项目中的数据和配置文件。

### `year.js`

记录当前网站使用的年份。

例如：

```text
2027
```

网站就显示并按照 2027 年进行相关处理。

每年更新项目时，需要根据实际年份修改这个文件。

### `mark.js`

记录当前年份的最低分数线。

例如：

```text
year.js
```

记录的是 2027 年，那么 `mark.js` 就应当记录 2027 年的最低分数线。

这个数据需要从官方渠道获取后手动修改。

### `bar.xlsx`

上一年度各个院校的分数线数据。

年份由：

```text
year.js - 1
```

确定。

例如：

```text
year.js = 2027
```

那么 `bar.xlsx` 应当保存 2026 年各院校分数线。

如果官方提供的是扫描版 PDF，可以先下载 PDF，再通过 OCR 或 AI 整理成 Excel。

### `bar.py`

将 `bar.xlsx` 中的上一年度院校分数线加入 `bar.js`。

程序根据 `year.js` 自动确定数据年份：

```text
年份 = year.js - 1
```

运行：

```bash
python bar.py
```

程序会保留 `bar.js` 中已有的历史数据，不应删除往年数据。

### `bar.js`

记录历年各院校分数线。

这个文件必须存在。

即使暂时没有历史数据，也应保留一个有效的空数据文件，否则 `index.html` 可能无法正常使用。

### `啟動網站.bat`

Windows 快速启动网站的批处理文件。

Windows 用户可以直接双击它启动本地网站。

### `实测.png`

`crawl_lzks.py` 的爬虫运行实测截图。

目前实测爬虫运行时间约为 1 分钟左右，实际运行时间会受到网络和官方网站服务器状态等因素影响。

## 三、完整更新流程

每年更新数据时按照以下顺序操作：

```text
① 修改 year.js
        ↓
② 安装 Python 依赖
        ↓
③ 运行 crawl_lzks.py
        ↓
④ 生成 / 更新 data.js
        ↓
⑤ 从官方渠道获得当前年份最低分数线
        ↓
⑥ 手动修改 mark.js
        ↓
⑦ 从官方渠道获得上一年度各院校分数线 PDF
        ↓
⑧ 将 PDF 整理为 bar.xlsx
        ↓
⑨ 运行 bar.py
        ↓
⑩ 更新 bar.js
        ↓
⑪ 启动网站
        ↓
⑫ 浏览器访问 index.html
```

## 四、Windows 用户

Windows 详细操作说明：

```text
readme/README-Windows.md
```

包括 Python 安装、CMD 操作、依赖安装、爬虫运行、分数线更新以及本地网站启动。

## 五、Android / Termux 用户

Termux 详细操作说明：

```text
readme/README-Termux.md
```

包括 Python、Git、依赖安装、项目下载、爬虫运行、数据更新以及本地 HTTP 网站启动。

## 六、网站无法正常读取数据时

如果直接打开：

```text
index.html
```

页面可以显示，但是数据无法正常读取，可以启动本地 HTTP 服务。

进入项目目录后运行：

```bash
python -m http.server 8000
```

然后使用浏览器访问：

```text
http://127.0.0.1:8000
```

这样网页通过 HTTP 运行，可以解决部分浏览器直接打开本地 HTML 时产生的文件读取或跨域限制。

Windows 也可以直接双击：

```text
啟動網站.bat
```

## 七、每年如何更新

假设新一年的实际年份为 2027。

### 1. 修改 `year.js`

设置为：

```text
2027
```

### 2. 更新招生数据

运行：

```bash
python crawl_lzks.py
```

完成后得到最新的：

```text
data.js
```

### 3. 更新最低分数线

从广东省教育考试院等官方渠道获得当前年份最低分数线。

手动修改：

```text
mark.js
```

### 4. 准备上一年度分数线

计算：

```text
2027 - 1 = 2026
```

所以准备：

```text
2026 年各院校分数线
```

下载官方 PDF。

如果 PDF 是扫描件：

```text
PDF
↓
OCR
↓
AI 整理
↓
Excel
↓
bar.xlsx
```

### 5. 更新历年分数线

运行：

```bash
python bar.py
```

程序把 `bar.xlsx` 的数据加入：

```text
bar.js
```

并保留以前的数据。

### 6. 启动网站

Windows：

```text
双击 啟動網站.bat
```

或者：

```bash
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

## 八、数据关系

```text
官方网站
    │
    ▼
crawl_lzks.py
    │
    ▼
data.js
    │
    ▼
index.html


year.js
    │
    ├──────────────► 当前网站年份
    │
    └── year.js - 1
              │
              ▼
           bar.xlsx
              │
              ▼
            bar.py
              │
              ▼
            bar.js
              │
              ▼
          index.html


官方当前年份最低分数线
              │
              ▼
           mark.js
              │
              ▼
          index.html
```

## 九、注意事项

- `year.js` 应根据实际年份修改。
- `crawl_lzks.py` 获取的是爬虫运行时官方网站上的数据。
- `data.js` 是爬虫生成的数据文件。
- `mark.js` 需要根据官方公布的最低分数线手动更新。
- `bar.xlsx` 应当对应 `year.js - 1` 年的数据。
- `bar.py` 用于把上一年度数据加入 `bar.js`。
- `bar.py` 不应删除已经存在的历史数据。
- `bar.js` 必须保留。
- 官方网站结构发生变化后，爬虫可能需要相应修改。
- 分数线数据应尽量使用官方来源。
- 如果直接打开 `index.html` 出现数据读取问题，使用 `python -m http.server 8000`。
