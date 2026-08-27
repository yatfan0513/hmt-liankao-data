# HMT 联考招生数据

港澳台联考招生数据爬虫与本地查询工具。

本项目用于获取港澳台联考招生数据，并生成本地查询网页。

支持：

- Windows + Python
- Android + Termux
- 本地查询
- Python 本地 HTTP 服务器
- 手动更新网页显示年份
- 手动更新最低分数线

---

## 一、项目结构

项目目录：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    ├── year.js
    ├── mark.js
    └── 实测.png

运行 `crawl_lzks.py` 后，会自动生成：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    ├── year.js
    ├── mark.js
    ├── 实测.png
    └── data.js

### 文件说明

| 文件 | 作用 |
|---|---|
| `crawl_lzks.py` | 招生数据爬虫 |
| `index.html` | 招生数据查询网页 |
| `data.js` | 爬虫运行后自动生成的招生数据 |
| `year.js` | 设置网页显示的年份 |
| `mark.js` | 设置网页显示的最低分数线 |
| `实测.png` | 爬虫运行实测截图 |

`data.js` 不需要手动创建。

---

# 二、项目工作流程

整个项目的工作流程：

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
    读取 year.js
          ↓
    读取 mark.js
          ↓
    浏览器显示招生数据

其中：

- `crawl_lzks.py` 负责获取招生数据；
- `data.js` 保存爬虫获取的数据；
- `index.html` 负责显示和查询数据；
- `year.js` 控制网页显示的年份；
- `mark.js` 控制网页显示的最低分数线。

---

# 三、Windows 使用

## 1. 安装 Python

如果电脑没有 Python，请访问：

    https://www.python.org/

下载安装 Python。

安装过程中建议勾选：

    Add Python to PATH

然后完成安装。

---

## 2. 检查 Python

按：

    Win + R

输入：

    cmd

按 Enter。

输入：

    python --version

如果出现类似：

    Python 3.12.10

说明 Python 安装成功。

---

## 3. 安装依赖

在 CMD 中输入：

    pip install requests beautifulsoup4 tqdm

如果 `pip` 无法使用：

    python -m pip install requests beautifulsoup4 tqdm

本项目需要：

    requests
    beautifulsoup4
    tqdm

不需要安装：

    pandas
    openpyxl

---

## 4. 放置项目

例如将项目放在：

    C:\Users\ABC\Documents\hmt-liankao-data\

这里的 `ABC` 只是示例，请替换成自己的 Windows 用户名。

确保目录中有：

    hmt-liankao-data/
    ├── crawl_lzks.py
    ├── index.html
    ├── year.js
    ├── mark.js
    └── 实测.png

---

## 5. 运行爬虫

打开 CMD。

输入：

    cd C:\Users\ABC\Documents\hmt-liankao-data

然后：

    python crawl_lzks.py

等待程序运行完成。

根据目前实际测试：

    爬虫运行时间约 1 分钟

实际时间会受到网络速度和目标网站响应速度影响。

运行期间：

- 不要关闭 CMD；
- 不要随意终止程序；
- 保持网络连接。

完成后会自动生成：

    data.js

---

# 四、修改网页显示年份

项目中的：

    year.js

用于控制网页显示的年份。

例如，如果 `year.js` 中设置为：

    1997

那么网页显示：

    1997

如果需要显示 2027，则把 `year.js` 修改为：

    2027

### 注意

`year.js` 只负责控制网页显示的年份。

它不决定爬虫获取哪一年的数据。

爬虫获取的是运行时目标网站实际提供的数据。

因此更新数据时建议：

1. 运行 `crawl_lzks.py`；
2. 确认网站已经提供最新数据；
3. 修改 `year.js`；
4. 刷新网页。

---

# 五、修改最低分数线

项目中的：

    mark.js

用于记录网页显示的最低分数线。

最低分数线需要自行从官方渠道获取。

建议查看：

- 广东省教育考试院官方网站；
- 广东省教育考试院官方微信公众号。

确认官方公布的最新数据以后，手动修改：

    mark.js

修改完成后：

    index.html

就会显示新的最低分数线。

### 注意

`mark.js` 不是爬虫自动获取的。

需要人工从官方渠道确认以后再修改。

---

# 六、打开查询网页

爬虫完成以后，可以直接双击：

    index.html

使用 Chrome 或 Edge 打开。

如果网页正常显示数据，就可以直接使用。

---

# 七、如果双击 index.html 无法读取数据

部分浏览器会限制：

    file://

页面读取本地：

    data.js

可能出现：

- 页面可以打开，但是没有数据；
- 数据加载失败；
- CORS / 跨域错误；
- `data.js` 明明存在，但是网页无法读取。

这种情况下可以使用 Python 本地 HTTP 服务器。

---

# 八、使用 127.0.0.1:8000

进入项目目录：

    cd C:\Users\ABC\Documents\hmt-liankao-data

输入：

    python -m http.server 8000

看到：

    Serving HTTP on 0.0.0.0 port 8000 ...

以后不要关闭 CMD。

打开浏览器，输入：

    http://127.0.0.1:8000

也可以：

    http://localhost:8000

此时浏览器会通过 HTTP 服务器读取：

    index.html
    data.js
    year.js
    mark.js

注意：

    http://127.0.0.1:8000

不要输入：

    https://127.0.0.1:8000

---

# 九、关闭本地服务器

使用完成后回到 CMD。

按：

    Ctrl + C

即可停止服务器。

---

# 十、Windows 更新数据

以后更新招生数据：

    cd C:\Users\ABC\Documents\hmt-liankao-data

运行：

    python crawl_lzks.py

等待爬虫完成。

确认：

    data.js

已经重新生成。

然后检查：

    year.js

是否需要修改。

再从广东省教育考试院官方渠道确认最新最低分数线，并修改：

    mark.js

最后打开：

    index.html

如果网页没有读取数据：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 十一、Android Termux 使用

本项目支持 Android 手机通过 Termux 运行。

Termux：

    https://github.com/termux/termux-app

---

## 1. 更新 Termux

打开 Termux：

    pkg update

然后：

    pkg upgrade

如果询问：

    Do you want to continue? [Y/n]

输入：

    y

---

## 2. 安装 Python

    pkg install python

检查：

    python --version

---

## 3. 安装 Git

    pkg install git

---

## 4. 下载项目

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

进入：

    cd hmt-liankao-data

检查：

    ls

应该看到：

    crawl_lzks.py
    index.html
    year.js
    mark.js
    实测.png

---

## 5. 安装依赖

    pip install requests beautifulsoup4 tqdm

如果失败：

    python -m pip install requests beautifulsoup4 tqdm

---

## 6. 运行爬虫

    python crawl_lzks.py

等待完成。

实测运行时间：

    约 1 分钟

完成以后：

    ls

应该看到：

    crawl_lzks.py
    index.html
    year.js
    mark.js
    实测.png
    data.js

---

# 十二、Termux 修改年份

修改：

    year.js

例如需要显示：

    2027

就把 `year.js` 中的数字设置为：

    2027

修改后刷新网页即可。

---

# 十三、Termux 修改最低分数线

从广东省教育考试院官方网站或官方微信公众号确认最新分数线。

然后手动修改：

    mark.js

修改完成后刷新网页。

---

# 十四、Termux 启动网页

进入项目目录：

    cd hmt-liankao-data

运行：

    python -m http.server 8000

然后打开手机浏览器：

    http://127.0.0.1:8000

不要关闭 Termux。

---

# 十五、Termux 使用手机存储

如果需要让 Termux 访问手机文件：

    termux-setup-storage

允许存储权限。

Download 文件夹通常对应：

    ~/storage/downloads/

例如：

    内部存储/Download/hmt-liankao-data/

Termux 中：

    cd ~/storage/downloads/hmt-liankao-data

---

# 十六、推荐的手机目录

    内部存储/
    └── Download/
        └── hmt-liankao-data/
            ├── crawl_lzks.py
            ├── index.html
            ├── year.js
            ├── mark.js
            ├── 实测.png
            └── data.js

---

# 十七、手机完整操作

第一次：

    pkg update
    pkg upgrade
    pkg install python git

下载：

    git clone https://github.com/yatfan0513/hmt-liankao-data.git

进入：

    cd hmt-liankao-data

安装依赖：

    pip install requests beautifulsoup4 tqdm

运行：

    python crawl_lzks.py

启动网页：

    python -m http.server 8000

浏览器打开：

    http://127.0.0.1:8000

---

# 十八、常见问题

## Python 找不到

Windows：

重新安装 Python，并勾选：

    Add Python to PATH

Termux：

    pkg install python

---

## pip 找不到

Windows：

    python -m pip install requests beautifulsoup4 tqdm

Termux：

    python -m pip install requests beautifulsoup4 tqdm

---

## 缺少 requests

    pip install requests

## 缺少 bs4

    pip install beautifulsoup4

## 缺少 tqdm

    pip install tqdm

---

## data.js 没有生成

检查：

1. 是否进入了正确的项目目录；
2. 是否安装了依赖；
3. 是否运行：

       python crawl_lzks.py

4. 爬虫是否正常完成；
5. 网络是否正常。

---

## index.html 可以打开，但是没有数据

运行：

    python -m http.server 8000

然后访问：

    http://127.0.0.1:8000

---

## year.js 修改后没有变化

确认：

1. 修改的是项目目录中的 `year.js`；
2. 文件已经保存；
3. 浏览器已经刷新。

电脑可以使用：

    Ctrl + F5

手机直接刷新网页即可。

---

## mark.js 修改后没有变化

确认：

1. 修改的是项目目录中的 `mark.js`；
2. 文件已经保存；
3. 浏览器已经刷新。

---

# 十九、实测

项目中的：

    实测.png

记录了爬虫实际运行情况。

目前实测：

    爬虫运行时间约 1 分钟

实际时间可能因为网络和目标网站响应速度不同而有所变化。

---

# 二十、完整更新流程

每次更新招生数据：

    ① 运行 crawl_lzks.py
            ↓
    ② 等待爬虫完成
            ↓
    ③ 确认 data.js 已生成
            ↓
    ④ 检查 year.js
            ↓
    ⑤ 从广东省教育考试院官方渠道确认最低分数线
            ↓
    ⑥ 修改 mark.js
            ↓
    ⑦ 打开 index.html
            ↓
    ⑧ 如果无法读取数据，使用 127.0.0.1:8000

---

# 二十一、注意事项

1. 爬虫运行需要网络连接。
2. 运行爬虫时不要关闭 CMD 或 Termux。
3. 运行本地 HTTP 服务器时不要关闭 CMD 或 Termux。
4. `data.js` 由 `crawl_lzks.py` 自动生成。
5. `index.html`、`year.js`、`mark.js` 和 `data.js` 应位于同一个目录。
6. `year.js` 只控制网页显示的年份，不决定爬虫获取哪一年的数据。
7. `mark.js` 需要根据广东省教育考试院官方公布的数据手动更新。
8. `实测.png` 是爬虫运行的实测截图。
9. 本地服务器使用完成后可以按 `Ctrl+C` 停止。
10. 如果目标网站改版、接口变化或数据结构变化，爬虫代码可能需要修改。

本项目用于港澳台联考招生数据整理、查询、学习和研究。

使用本项目时，请遵守目标网站相关规定以及适用的法律法规。

标签信息来自网络，若有误可手动修改 `index.html` 。