# HMT 联考招生数据 — Android Termux

港澳台联考招生数据爬虫与本地查询网页。

本版本用于 Android 手机，通过 Termux 运行 Python 爬虫，生成 `data.js`，再通过手机浏览器访问本地网页。

## 项目结构

```text
hmt-liankao-data/
├── crawl_lzks.py
└── index.html
```

运行后：

```text
hmt-liankao-data/
├── crawl_lzks.py
├── index.html
└── data.js
```

- `crawl_lzks.py`：爬虫
- `index.html`：查询网页
- `data.js`：爬虫自动生成的数据文件

---

# 一、安装 Termux

建议使用官方项目：

https://github.com/termux/termux-app

安装并打开 Termux。

---

# 二、第一次使用

更新软件包：

```bash
pkg update
```

然后：

```bash
pkg upgrade
```

如果询问是否继续，输入：

```text
y
```

---

# 三、安装 Python

```bash
pkg install python
```

检查：

```bash
python --version
```

出现类似：

```text
Python 3.12.x
```

即可。

---

# 四、安装 Git

```bash
pkg install git
```

检查：

```bash
git --version
```

---

# 五、下载项目

输入：

```bash
git clone https://github.com/yatfan0513/hmt-liankao-data.git
```

进入：

```bash
cd hmt-liankao-data
```

检查：

```bash
ls
```

应看到：

```text
crawl_lzks.py
index.html
```

---

# 六、安装依赖

```bash
pip install requests beautifulsoup4 tqdm
```

如果 `pip` 无法使用：

```bash
python -m pip install requests beautifulsoup4 tqdm
```

---

# 七、运行爬虫

确保当前位于：

```text
hmt-liankao-data
```

运行：

```bash
python crawl_lzks.py
```

保持 Termux 打开，并保持网络连接。

等待爬虫完成。

然后：

```bash
ls
```

应该看到：

```text
crawl_lzks.py
index.html
data.js
```

---

# 八、推荐使用 127.0.0.1:8000

Android 浏览器直接打开本地 `file://` HTML 时，可能限制网页读取 `data.js`。

因此推荐使用 Python 本地 HTTP 服务器。

在项目目录运行：

```bash
python -m http.server 8000
```

看到类似：

```text
Serving HTTP on 0.0.0.0 port 8000 ...
```

后不要关闭 Termux。

打开手机浏览器，在地址栏输入：

```text
http://127.0.0.1:8000
```

然后访问。

此时：

```text
浏览器
  ↓
http://127.0.0.1:8000
  ↓
index.html
  ↓
data.js
```

这样通常可以解决直接打开 HTML 时的数据读取/跨域问题。

> 注意必须使用 `http://`，不是 `https://`。

---

# 九、停止服务器

使用完成后回到 Termux，按：

```text
Ctrl + C
```

停止服务器。

如果手机键盘没有 Ctrl，可使用 Termux 的额外按键功能发送 Ctrl+C。

下次使用：

```bash
python -m http.server 8000
```

即可重新启动。

---

# 十、使用手机共享存储

如果希望用 Android 文件管理器看到项目，可以执行：

```bash
termux-setup-storage
```

允许 Termux 访问文件。

手机的 Download 文件夹通常对应：

```text
~/storage/downloads/
```

例如项目放在：

```text
内部存储/Download/hmt-liankao-data/
```

Termux 中对应：

```text
~/storage/downloads/hmt-liankao-data/
```

进入：

```bash
cd ~/storage/downloads/hmt-liankao-data
```

检查：

```bash
ls
```

然后同样可以运行：

```bash
python crawl_lzks.py
```

---

# 十一、推荐的手机存储结构

```text
内部存储/
└── Download/
    └── hmt-liankao-data/
        ├── crawl_lzks.py
        ├── index.html
        └── data.js
```

这样方便：

- Termux 运行 Python
- 文件管理器查看文件
- 浏览器使用网页
- 备份项目

---

# 十二、从 GitHub 到网页的完整操作

第一次使用：

```bash
pkg update
pkg upgrade
pkg install python git
git clone https://github.com/yatfan0513/hmt-liankao-data.git
cd hmt-liankao-data
pip install requests beautifulsoup4 tqdm
python crawl_lzks.py
python -m http.server 8000
```

然后浏览器打开：

```text
http://127.0.0.1:8000
```

---

# 十三、以后更新数据

进入项目：

```bash
cd ~/hmt-liankao-data
```

重新运行：

```bash
python crawl_lzks.py
```

完成后：

```bash
python -m http.server 8000
```

浏览器访问：

```text
http://127.0.0.1:8000
```

如果显示旧数据，刷新浏览器页面。

---

# 十四、常见问题

### Python 找不到

```bash
pkg install python
```

### pip 找不到

```bash
python -m pip install requests beautifulsoup4 tqdm
```

### 缺少 requests

```bash
pip install requests
```

### 缺少 bs4

```bash
pip install beautifulsoup4
```

### 缺少 tqdm

```bash
pip install tqdm
```

### data.js 没有生成

重新运行：

```bash
python crawl_lzks.py
```

### 网页打开但没有数据

不要直接使用 `file://`。

进入项目目录：

```bash
python -m http.server 8000
```

然后打开：

```text
http://127.0.0.1:8000
```

### 127.0.0.1:8000 打不开

确认 Termux 中仍然显示：

```text
Serving HTTP on 0.0.0.0 port 8000 ...
```

如果服务器已经停止，重新运行：

```bash
python -m http.server 8000
```

确认浏览器输入的是：

```text
http://127.0.0.1:8000
```

而不是：

```text
https://127.0.0.1:8000
```

---

# 十五、最简操作

已经安装 Python、Git 和依赖后：

```bash
cd ~/hmt-liankao-data
python crawl_lzks.py
python -m http.server 8000
```

浏览器打开：

```text
http://127.0.0.1:8000
```

即可。

---

# 十六、注意事项

爬虫需要网络连接。

运行爬虫时不要关闭 Termux。

运行本地服务器时不要关闭 Termux，否则 `127.0.0.1:8000` 会停止。

本项目依赖目标网站当前的页面结构。网站改版或接口变化后，爬虫可能需要修改。

本项目用于招生数据整理、查询、学习和研究。使用时请遵守目标网站相关规定及适用法律法规。
