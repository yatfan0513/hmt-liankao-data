# HMT 联考招生数据 — Android Termux 使用指南

本文件专门介绍如何使用 Android 手机和 Termux 运行本项目。

---

# 一、你需要准备什么

需要：

1. Android 手机；
2. Termux；
3. 网络连接；
4. 本项目文件。

Termux 官方项目：

    https://github.com/termux/termux-app

Python 依赖：

    requests
    beautifulsoup4
    tqdm

---

# 二、安装 Termux

安装并打开 Termux。

建议使用 Termux 官方项目提供的版本。

---

# 三、更新 Termux

输入：

    pkg update

然后：

    pkg upgrade

如果出现：

    Do you want to continue? [Y/n]

输入：

    y

然后按 Enter。

---

# 四、安装 Python

输入：

    pkg install python

检查：

    python --version

如果出现：

    Python 3.x.x

说明 Python 安装成功。

---

# 五、安装 Git

输入：

    pkg install git

检查：

    git --version

---

# 六、下载项目

输入：

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

进入项目：

    cd hmt-liankao-data

输入：

    ls

应该看到：

    crawl_lzks.py
    index.html
    year.js
    mark.js
    实测.png

---

# 七、安装依赖

输入：

    pip install requests beautifulsoup4 tqdm

如果失败：

    python -m pip install requests beautifulsoup4 tqdm

---

# 八、运行爬虫

输入：

    python crawl_lzks.py

等待爬虫完成。

目前实测：

    约 1 分钟

实际时间可能受到：

- 网络速度；
- 目标网站响应速度；
- 手机性能

等因素影响。

运行过程中不要关闭 Termux。

---

# 九、确认 data.js

完成后输入：

    ls

应该看到：

    crawl_lzks.py
    index.html
    year.js
    mark.js
    实测.png
    data.js

---

# 十、修改年份

项目中的：

    year.js

负责控制网页显示的年份。

例如需要显示：

    2027

就修改 `year.js` 中的数字。

保存以后刷新网页即可。

注意：

`year.js` 不负责决定爬虫获取哪一年的数据。

它只控制网页显示的年份。

---

# 十一、修改最低分数线

打开：

    mark.js

从广东省教育考试院官方网站或者官方微信公众号获取最新最低分数线。

确认以后手动修改：

    mark.js

保存以后刷新网页。

---

# 十二、启动网页

进入项目目录：

    cd hmt-liankao-data

运行：

    python -m http.server 8000

如果看到：

    Serving HTTP on 0.0.0.0 port 8000 ...

说明服务器启动成功。

不要关闭 Termux。

---

# 十三、打开网页

打开手机浏览器。

输入：

    http://127.0.0.1:8000

即可打开：

    index.html

网页会读取：

    data.js
    year.js
    mark.js

---

# 十四、为什么使用 127.0.0.1:8000

Android 浏览器直接打开：

    file://

格式的 HTML 时，有时会限制网页读取本地 JavaScript 文件。

因此推荐：

    python -m http.server 8000

然后使用：

    http://127.0.0.1:8000

这样网页通过 HTTP 访问本地文件。

---

# 十五、注意 http 和 https

正确：

    http://127.0.0.1:8000

错误：

    https://127.0.0.1:8000

必须使用：

    http://

---

# 十六、停止服务器

回到 Termux。

按：

    Ctrl + C

即可停止。

如果手机键盘没有 Ctrl，可以使用 Termux 的额外按键功能发送 Ctrl+C。

---

# 十七、让 Termux 访问手机文件

输入：

    termux-setup-storage

Android 会请求存储权限。

允许。

以后：

    ~/storage/

就是 Termux 可以访问的手机存储目录。

Download 通常是：

    ~/storage/downloads/

---

# 十八、把项目放到 Download

推荐：

    内部存储/
    └── Download/
        └── hmt-liankao-data/
            ├── crawl_lzks.py
            ├── index.html
            ├── year.js
            ├── mark.js
            ├── 实测.png
            └── data.js

Termux 中进入：

    cd ~/storage/downloads/hmt-liankao-data

检查：

    ls

---

# 十九、从手机文件夹运行

如果项目在 Download：

    cd ~/storage/downloads/hmt-liankao-data

运行爬虫：

    python crawl_lzks.py

完成后：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 二十、手机完整操作

第一次：

    pkg update
    pkg upgrade
    pkg install python git

下载：

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

进入：

    cd hmt-liankao-data

安装：

    pip install requests beautifulsoup4 tqdm

运行：

    python crawl_lzks.py

启动网页：

    python -m http.server 8000

浏览器：

    http://127.0.0.1:8000

---

# 二十一、以后更新数据

进入项目：

    cd ~/hmt-liankao-data

运行：

    python crawl_lzks.py

等待完成。

确认：

    data.js

已经生成。

然后检查：

    year.js

是否需要修改。

从广东省教育考试院官方渠道确认最新最低分数线。

修改：

    mark.js

最后：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 二十二、常见问题

## Python 找不到

输入：

    pkg install python

---

## pip 找不到

输入：

    python -m pip install requests beautifulsoup4 tqdm

---

## 缺少 requests

    pip install requests

---

## 缺少 bs4

    pip install beautifulsoup4

---

## 缺少 tqdm

    pip install tqdm

---

## data.js 没有生成

检查当前目录：

    pwd

然后：

    ls

确认存在：

    crawl_lzks.py

再运行：

    python crawl_lzks.py

---

## 网页没有数据

运行：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

## 127.0.0.1:8000 打不开

检查 Termux 是否仍然显示：

    Serving HTTP on 0.0.0.0 port 8000 ...

如果没有，重新运行：

    python -m http.server 8000

确认浏览器输入：

    http://127.0.0.1:8000

而不是：

    https://127.0.0.1:8000

---

## year.js 修改后没有变化

保存 `year.js` 后刷新网页。

---

## mark.js 修改后没有变化

保存 `mark.js` 后刷新网页。

---

# 二十三、实测

项目中的：

    实测.png

是爬虫运行的实际截图。

目前实测运行时间：

    约 1 分钟

实际运行时间可能有所不同。

---

# 二十四、注意

- 爬虫需要网络；
- 运行爬虫时不要关闭 Termux；
- 运行 HTTP 服务器时不要关闭 Termux；
- `data.js` 由爬虫自动生成；
- `year.js` 控制网页显示年份；
- `mark.js` 控制网页显示最低分数线；
- 最低分数线需要从广东省教育考试院官方渠道确认；
- `index.html`、`year.js`、`mark.js`、`data.js` 应位于同一个项目目录；
- 本地服务器使用完成后按 `Ctrl+C` 停止。

本项目用于港澳台联考招生数据整理、查询、学习和研究。

标签信息来自网络，若有误可手动修改 `index.html` 。