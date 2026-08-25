# HMT 联考招生数据

港澳台联考招生数据爬虫与本地查询网页。

## 项目结构

```text
hmt-liankao-data/
├── crawl_lzks.py
└── index.html
```

运行爬虫后会自动生成：

```text
hmt-liankao-data/
├── crawl_lzks.py
├── index.html
└── data.js
```

- `crawl_lzks.py`：爬取招生数据并生成 `data.js`
- `index.html`：招生数据查询页面
- `data.js`：爬虫生成的数据文件，不需要手动创建

---

# 一、Windows 使用

## 1. 安装 Python

前往：

https://www.python.org/

安装时勾选：

```text
Add Python to PATH
```

安装完成后按 `Win + R`，输入：

```text
cmd
```

按 Enter。

检查：

```cmd
python --version
```

出现类似 `Python 3.12.10` 即可。

## 2. 安装依赖

在 CMD 输入：

```cmd
pip install requests beautifulsoup4 tqdm
```

如果 `pip` 无法使用：

```cmd
python -m pip install requests beautifulsoup4 tqdm
```

本项目需要：

```text
requests
beautifulsoup4
tqdm
```

## 3. 下载项目

将 `hmt-liankao-data` 放到电脑，例如：

```text
C:\Users\ABC\Documents\hmt-liankao-data\
```

也可以放在：

```text
C:\Users\ABC\Desktop\hmt-liankao-data\
```

`ABC` 只是示例，请替换成你的实际 Windows 用户名。

项目文件夹中应有：

```text
hmt-liankao-data/
├── crawl_lzks.py
└── index.html
```

## 4. 运行爬虫

打开 CMD：

```cmd
cd C:\Users\ABC\Documents\hmt-liankao-data
```

检查：

```cmd
dir
```

然后运行：

```cmd
python crawl_lzks.py
```

等待爬虫完成，不要关闭 CMD，并保持网络连接。

完成后会生成：

```text
data.js
```

## 5. 打开网页

直接双击：

```text
index.html
```

即可使用。

推荐使用 Chrome 或 Edge。

---

# 二、如果双击后数据无法读取

部分浏览器会限制 `file://` 页面读取本地 `data.js`。

如果出现：

- 页面能打开但没有数据
- 数据加载失败
- 浏览器提示跨域/CORS
- `data.js` 明明存在但无法读取

使用 Python 本地 HTTP 服务器。

进入项目目录：

```cmd
cd C:\Users\ABC\Documents\hmt-liankao-data
```

运行：

```cmd
python -m http.server 8000
```

看到类似：

```text
Serving HTTP on 0.0.0.0 port 8000 ...
```

后不要关闭 CMD。

打开 Chrome 或 Edge，在地址栏输入：

```text
http://127.0.0.1:8000
```

也可以：

```text
http://localhost:8000
```

即可正常打开 `index.html` 并读取 `data.js`。

使用完成后回到 CMD，按：

```text
Ctrl + C
```

即可关闭服务器。

---

# 三、更新数据

以后需要重新获取数据：

```cmd
cd C:\Users\ABC\Documents\hmt-liankao-data
python crawl_lzks.py
```

完成后重新打开 `index.html`。

如果显示旧数据，按：

```text
Ctrl + F5
```

强制刷新。

如果使用本地服务器：

```cmd
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

---

# 四、Windows 最简命令

```cmd
pip install requests beautifulsoup4 tqdm
cd C:\Users\ABC\Documents\hmt-liankao-data
python crawl_lzks.py
```

然后双击 `index.html`。

如果打不开数据：

```cmd
python -m http.server 8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

---

# 五、常见问题

### Python 找不到

重新安装 Python，并勾选 `Add Python to PATH`。

### pip 找不到

```cmd
python -m pip install requests beautifulsoup4 tqdm
```

### 缺少 requests

```cmd
pip install requests
```

### 缺少 bs4

```cmd
pip install beautifulsoup4
```

### 缺少 tqdm

```cmd
pip install tqdm
```

### data.js 没有生成

确认进入了正确的项目目录，并运行：

```cmd
python crawl_lzks.py
```

### index.html 没有数据

运行：

```cmd
python -m http.server 8000
```

然后访问：

```text
http://127.0.0.1:8000
```

---

# 六、注意事项

爬虫需要网络连接。

运行爬虫时不要关闭 CMD。

运行本地服务器时不要关闭 CMD，否则 `127.0.0.1:8000` 会停止。

本项目依赖目标网站当前的页面结构。网站改版或接口变化后，爬虫可能需要修改。

本项目用于招生数据整理、查询、学习和研究。使用时请遵守目标网站相关规定及适用法律法规。
