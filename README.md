# HMT 联考招生数据

港澳台联考招生数据爬虫与本地查询工具。

本项目可以从相关招生网站获取招生数据，并生成 `data.js`，然后通过 `index.html` 在浏览器中进行本地查询。

支持：

- Windows + Python
- Android + Termux
- 本地查询
- Python 本地 HTTP 服务器 `127.0.0.1:8000`

---

## 一、项目结构

项目下载后：

    hmt-liankao-data/
    ├── crawl_lzks.py
    └── index.html

运行 `crawl_lzks.py` 后：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    └── data.js

文件作用：

| 文件 | 作用 |
|---|---|
| `crawl_lzks.py` | 招生数据爬虫，运行后生成 `data.js` |
| `index.html` | 招生数据查询页面 |
| `data.js` | 爬虫生成的招生数据 |

`data.js` 不需要手动创建。

---

## 二、工作流程

整个项目的流程：

    crawl_lzks.py
          ↓
    访问招生网站
          ↓
    获取招生数据
          ↓
    生成 data.js
          ↓
    index.html 读取 data.js
          ↓
    浏览器打开 index.html
          ↓
    查询招生数据

如果浏览器直接打开 `index.html` 后无法读取 `data.js`，可以启动 Python 本地 HTTP 服务器：

    crawl_lzks.py
          ↓
       data.js
          ↓
    Python HTTP Server
          ↓
    http://127.0.0.1:8000
          ↓
       index.html
          ↓
       查询数据

---

# Windows 版本

## 三、安装 Python

如果电脑还没有安装 Python，请前往：

https://www.python.org/

下载安装。

安装过程中建议勾选：

    Add Python to PATH

然后完成安装。

---

## 四、检查 Python

按键盘：

    Win + R

输入：

    cmd

按 Enter。

在 CMD 中输入：

    python --version

如果出现类似：

    Python 3.12.10

说明 Python 安装成功。

---

## 五、安装 Python 依赖

在 CMD 中输入：

    pip install requests beautifulsoup4 tqdm

如果 `pip` 无法使用，则输入：

    python -m pip install requests beautifulsoup4 tqdm

本项目需要的依赖只有：

    requests
    beautifulsoup4
    tqdm

不需要安装 `pandas` 或 `openpyxl`。

---

## 六、下载项目

从 GitHub 下载本项目：

    hmt-liankao-data

例如，可以把项目放在：

    C:\Users\ABC\Documents\hmt-liankao-data\

也可以放在：

    C:\Users\ABC\Desktop\hmt-liankao-data\

这里的 `ABC` 只是示例，请根据自己的电脑实际用户名修改。

例如：

    C:\Users\ABC\Documents\hmt-liankao-data\
    ├── crawl_lzks.py
    └── index.html

---

## 七、运行爬虫

### 1. 打开 CMD

按：

    Win + R

输入：

    cmd

按 Enter。

### 2. 进入项目文件夹

如果项目位于：

    C:\Users\ABC\Documents\hmt-liankao-data

输入：

    cd C:\Users\ABC\Documents\hmt-liankao-data

如果你的项目放在其他位置，请把路径修改成实际路径。

### 3. 检查文件

输入：

    dir

应该看到：

    crawl_lzks.py
    index.html

### 4. 运行爬虫

输入：

    python crawl_lzks.py

按 Enter。

等待爬虫完成。

运行过程中：

- 不要关闭 CMD
- 不要随意终止程序
- 保持网络连接

---

## 八、爬虫完成后

运行完成后，会自动在项目文件夹生成：

    data.js

最终目录：

    C:\Users\ABC\Documents\hmt-liankao-data\
    ├── crawl_lzks.py
    ├── index.html
    └── data.js

---

## 九、打开查询网页

爬虫完成后，最简单的方法是：

双击：

    index.html

推荐使用：

- Microsoft Edge
- Google Chrome

如果网页正常显示数据，就可以直接使用。

---

## 十、如果双击 index.html 后无法读取数据

部分浏览器会限制通过：

    file://

直接打开的网页读取本地 `data.js`。

可能出现：

- 页面可以打开，但没有数据
- 数据加载失败
- 浏览器控制台出现 CORS / 跨域错误
- `data.js` 明明存在，但是网页无法读取

这时候不需要修改 `index.html`。

可以使用 Python 启动本地 HTTP 服务器。

---

## 十一、使用 127.0.0.1:8000

首先进入项目文件夹。

例如：

    cd C:\Users\ABC\Documents\hmt-liankao-data

然后输入：

    python -m http.server 8000

如果成功，会看到类似：

    Serving HTTP on 0.0.0.0 port 8000 ...

不要关闭这个 CMD 窗口。

然后打开 Chrome 或 Edge。

在地址栏输入：

    http://127.0.0.1:8000

按 Enter。

也可以输入：

    http://localhost:8000

浏览器会通过本地 HTTP 服务器打开：

    index.html

并读取：

    data.js

这样通常可以解决直接双击 HTML 时的数据读取和跨域问题。

注意必须使用：

    http://127.0.0.1:8000

不要使用：

    https://127.0.0.1:8000

---

## 十二、关闭本地服务器

使用完成后回到 CMD。

按：

    Ctrl + C

即可停止服务器。

以后再次需要使用时，重新输入：

    python -m http.server 8000

即可。

---

## 十三、Windows 更新招生数据

以后需要重新获取网站上的数据时，不需要重新下载项目。

进入项目：

    cd C:\Users\ABC\Documents\hmt-liankao-data

运行：

    python crawl_lzks.py

等待爬虫完成。

新的：

    data.js

会自动生成。

然后重新打开：

    index.html

如果浏览器仍然显示旧数据，可以按：

    Ctrl + F5

强制刷新。

如果使用本地服务器：

    python -m http.server 8000

然后访问：

    http://127.0.0.1:8000

---

## 十四、Windows 完整示例

假设项目位置：

    C:\Users\ABC\Documents\hmt-liankao-data

第一次安装依赖：

    pip install requests beautifulsoup4 tqdm

进入项目：

    cd C:\Users\ABC\Documents\hmt-liankao-data

运行爬虫：

    python crawl_lzks.py

等待完成。

然后：

    data.js

会自动出现。

如果双击 `index.html` 可以正常使用：

    双击 index.html

如果双击后没有数据：

    python -m http.server 8000

然后浏览器访问：

    http://127.0.0.1:8000

---

# Android Termux 版本

## 十五、安装 Termux

本项目可以在 Android 手机上使用 Termux 运行。

建议使用 Termux 官方项目：

https://github.com/termux/termux-app

安装完成后打开 Termux。

---

## 十六、第一次使用 Termux

打开 Termux 后，先更新软件包：

    pkg update

然后：

    pkg upgrade

如果询问：

    Do you want to continue? [Y/n]

输入：

    y

然后按 Enter。

---

## 十七、安装 Python

输入：

    pkg install python

安装完成后检查：

    python --version

如果出现类似：

    Python 3.12.x

说明 Python 安装成功。

---

## 十八、安装 Git

如果准备直接从 GitHub 下载项目：

    pkg install git

检查：

    git --version

---

## 十九、从 GitHub 下载项目

输入：

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

下载完成后：

    cd hmt-liankao-data

检查文件：

    ls

应该看到：

    crawl_lzks.py
    index.html

---

## 二十、安装 Python 依赖

输入：

    pip install requests beautifulsoup4 tqdm

如果 `pip` 无法使用：

    python -m pip install requests beautifulsoup4 tqdm

---

## 二十一、运行爬虫

确保当前目录是：

    hmt-liankao-data

运行：

    python crawl_lzks.py

等待爬虫完成。

完成后输入：

    ls

应该看到：

    crawl_lzks.py
    index.html
    data.js

说明爬虫已经生成数据。

---

## 二十二、Termux 中为什么推荐 127.0.0.1:8000

Android 浏览器直接打开：

    file://

格式的 HTML 时，有时会限制网页读取同目录中的：

    data.js

因此推荐使用 Python 本地 HTTP 服务器。

在项目目录中运行：

    python -m http.server 8000

如果成功，会看到类似：

    Serving HTTP on 0.0.0.0 port 8000 ...

不要关闭 Termux。

打开手机浏览器，在地址栏输入：

    http://127.0.0.1:8000

即可打开查询页面。

网页加载关系：

    浏览器
       ↓
    http://127.0.0.1:8000
       ↓
    index.html
       ↓
    data.js

这样通常可以解决直接打开 HTML 时的数据读取和跨域问题。

注意：

    http://127.0.0.1:8000

必须使用 `http://`。

不要输入：

    https://127.0.0.1:8000

---

## 二十三、关闭 Termux 本地服务器

使用完成以后回到 Termux。

按：

    Ctrl + C

即可停止服务器。

如果手机键盘没有 Ctrl，可以使用 Termux 的额外按键功能发送 `Ctrl+C`。

以后再次使用：

    python -m http.server 8000

即可。

---

## 二十四、Termux 使用手机共享存储

如果希望通过 Android 文件管理器查看项目，可以输入：

    termux-setup-storage

Android 会弹出存储权限请求。

允许 Termux 访问文件。

之后可以访问：

    ~/storage/

手机的 Download 文件夹通常对应：

    ~/storage/downloads/

例如项目位于：

    内部存储/Download/hmt-liankao-data/

Termux 中可以进入：

    cd ~/storage/downloads/hmt-liankao-data

然后：

    ls

应该看到：

    crawl_lzks.py
    index.html

---

## 二十五、推荐的手机目录

推荐将项目放在：

    内部存储/
    └── Download/
        └── hmt-liankao-data/
            ├── crawl_lzks.py
            ├── index.html
            └── data.js

这样方便：

- Termux 运行 Python
- Android 文件管理器查看文件
- 浏览器打开网页
- 备份项目

---

## 二十六、Termux 完整操作

第一次使用：

    pkg update
    pkg upgrade
    pkg install python git

下载项目：

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

进入项目：

    cd hmt-liankao-data

安装依赖：

    pip install requests beautifulsoup4 tqdm

运行爬虫：

    python crawl_lzks.py

启动本地服务器：

    python -m http.server 8000

然后打开手机浏览器：

    http://127.0.0.1:8000

即可使用。

---

## 二十七、Termux 更新数据

进入项目：

    cd ~/hmt-liankao-data

运行：

    python crawl_lzks.py

等待完成。

启动本地服务器：

    python -m http.server 8000

然后打开：

    http://127.0.0.1:8000

如果网页仍显示旧数据，刷新浏览器。

---

# 常见问题

## 1. Python 找不到

Windows：

重新安装 Python，并勾选：

    Add Python to PATH

Termux：

    pkg install python

---

## 2. pip 找不到

Windows：

    python -m pip install requests beautifulsoup4 tqdm

Termux：

    python -m pip install requests beautifulsoup4 tqdm

---

## 3. 缺少 requests

    pip install requests

## 4. 缺少 bs4

    pip install beautifulsoup4

## 5. 缺少 tqdm

    pip install tqdm

---

## 6. data.js 没有生成

确认：

1. 已经进入正确的 `hmt-liankao-data` 文件夹；
2. 已经安装依赖；
3. 已经运行：

       python crawl_lzks.py

4. 爬虫已经正常完成；
5. 设备可以正常连接网络。

---

## 7. index.html 可以打开，但是没有数据

不要继续直接使用：

    file://

改用本地 HTTP 服务器。

Windows 和 Termux 都可以运行：

    python -m http.server 8000

然后浏览器打开：

    http://127.0.0.1:8000

---

## 8. 127.0.0.1:8000 打不开

首先检查 CMD 或 Termux 中是否仍然显示：

    Serving HTTP on 0.0.0.0 port 8000 ...

如果服务器已经停止，重新运行：

    python -m http.server 8000

确认浏览器地址是：

    http://127.0.0.1:8000

而不是：

    https://127.0.0.1:8000

---

# 最简操作

## Windows

已经安装 Python 和依赖：

    cd C:\Users\ABC\Documents\hmt-liankao-data
    python crawl_lzks.py

然后双击：

    index.html

如果无法读取数据：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

## Android Termux

已经安装 Python、Git 和依赖：

    cd ~/hmt-liankao-data
    python crawl_lzks.py
    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 注意事项

1. 爬虫运行需要网络连接。
2. 运行爬虫时不要关闭 CMD 或 Termux。
3. 运行本地 HTTP 服务器时不要关闭 CMD 或 Termux。
4. `data.js` 是爬虫自动生成的，不需要手动创建或编辑。
5. `index.html` 和 `data.js` 必须位于同一个文件夹。
6. 本地服务器使用完成后可以按 `Ctrl+C` 停止。
7. 项目依赖目标网站当前的页面结构。
8. 如果目标网站改版、接口变化或数据结构变化，`crawl_lzks.py` 可能需要修改。

本项目用于港澳台联考招生数据整理、查询、学习和研究。

使用本项目时，请遵守目标网站相关规定以及适用的法律法规。
