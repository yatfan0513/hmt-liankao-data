# HMT 联考招生数据 — Windows 使用指南

本文件专门介绍如何在 Windows 电脑上运行本项目。

---

# 一、你需要准备什么

只需要：

1. 一台 Windows 电脑；
2. Python；
3. 网络连接；
4. 本项目文件。

需要安装的 Python 依赖：

    requests
    beautifulsoup4
    tqdm

---

# 二、安装 Python

打开：

    https://www.python.org/

下载安装 Python。

安装时一定建议勾选：

    Add Python to PATH

安装完成以后关闭安装程序。

---

# 三、检查 Python

按：

    Win + R

输入：

    cmd

按 Enter。

输入：

    python --version

如果出现：

    Python 3.x.x

说明 Python 已经安装成功。

---

# 四、安装依赖

在 CMD 输入：

    pip install requests beautifulsoup4 tqdm

如果提示 pip 不存在：

    python -m pip install requests beautifulsoup4 tqdm

安装完成即可。

---

# 五、准备项目文件

例如把项目放在：

    C:\Users\ABC\Documents\hmt-liankao-data\

其中 `ABC` 只是示例。

项目目录应该有：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    ├── year.js
    ├── mark.js
    └── 实测.png

---

# 六、进入项目目录

按：

    Win + R

输入：

    cmd

按 Enter。

输入：

    cd C:\Users\ABC\Documents\hmt-liankao-data

然后输入：

    dir

确认能够看到：

    crawl_lzks.py
    index.html
    year.js
    mark.js
    实测.png

---

# 七、运行爬虫

输入：

    python crawl_lzks.py

然后等待。

目前实际测试：

    约 1 分钟

具体时间取决于网络和目标网站响应速度。

运行过程中不要关闭 CMD。

---

# 八、确认 data.js

爬虫完成以后，输入：

    dir

应该出现：

    data.js

最终：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    ├── year.js
    ├── mark.js
    ├── 实测.png
    └── data.js

---

# 九、修改年份

打开：

    year.js

例如：

    2027

网页就会显示 2027。

如果需要显示其他年份，就修改这个数字。

注意：

`year.js` 只负责网页显示的年份。

它不会改变爬虫获取的数据。

---

# 十、修改最低分数线

打开：

    mark.js

从广东省教育考试院官方网站或者官方微信公众号查看最新最低分数线。

确认以后手动修改 `mark.js`。

保存文件。

网页刷新后即可显示新的最低分数线。

---

# 十一、打开网页

直接双击：

    index.html

如果网页正常显示数据，可以直接使用。

---

# 十二、如果网页没有数据

如果出现：

    页面可以打开，但是没有数据

或者：

    data.js 无法读取

使用本地服务器。

先进入项目目录：

    cd C:\Users\ABC\Documents\hmt-liankao-data

然后：

    python -m http.server 8000

看到：

    Serving HTTP on 0.0.0.0 port 8000 ...

不要关闭 CMD。

打开浏览器：

    http://127.0.0.1:8000

即可。

---

# 十三、为什么使用 127.0.0.1:8000

直接双击 HTML 时，浏览器使用：

    file://

有些浏览器会限制网页读取本地 JavaScript 数据文件。

使用：

    http://127.0.0.1:8000

以后，网页就通过本地 HTTP 服务器访问。

因此：

    index.html
    data.js
    year.js
    mark.js

可以正常加载。

---

# 十四、关闭服务器

使用完成以后回到 CMD。

按：

    Ctrl + C

即可。

---

# 十五、以后更新数据

进入项目：

    cd C:\Users\ABC\Documents\hmt-liankao-data

运行：

    python crawl_lzks.py

等待完成。

确认生成：

    data.js

然后检查：

    year.js

再从广东省教育考试院官方渠道确认最新最低分数线。

修改：

    mark.js

最后打开：

    index.html

如果无法读取数据：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 十六、Windows 最简操作

安装依赖：

    pip install requests beautifulsoup4 tqdm

进入目录：

    cd C:\Users\ABC\Documents\hmt-liankao-data

运行：

    python crawl_lzks.py

修改：

    year.js
    mark.js

打开：

    index.html

如果无法读取数据：

    python -m http.server 8000

浏览器：

    http://127.0.0.1:8000

---

# 十七、常见问题

## Python 找不到

重新安装 Python，并勾选：

    Add Python to PATH

---

## pip 找不到

使用：

    python -m pip install requests beautifulsoup4 tqdm

---

## data.js 没有生成

重新进入项目目录：

    cd C:\Users\ABC\Documents\hmt-liankao-data

然后：

    python crawl_lzks.py

---

## 网页没有数据

使用：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

## 网页年份没有变化

修改：

    year.js

保存以后刷新网页。

电脑可以按：

    Ctrl + F5

---

## 最低分数线没有变化

修改：

    mark.js

保存以后刷新网页。

---

# 十八、注意

- `data.js` 不需要手动创建；
- `data.js` 是 `crawl_lzks.py` 自动生成的；
- `year.js` 控制网页显示年份；
- `mark.js` 控制网页显示最低分数线；
- 最低分数线应从广东省教育考试院官方渠道确认；
- 爬虫运行需要网络；
- 运行服务器时不能关闭 CMD。

本项目用于港澳台联考招生数据整理、查询、学习和研究。

标签信息来自网络，若有误可手动修改 `index.html` 。