# matplotlib 中文顯示問題

https://daxpowerbi.com/如何在win-10解決matplotlib中文顯示的問題/

## TL;DR

先下載 `SimHei.ttf` 字體並安裝，之後將 `SimHei.ttf` 拷貝到python安裝路徑 `/site-packages/matplotlib/mpl-data/fonts/ttf` 目錄中

修改python安装路径 `/site-packages/matplotlib/mpl-data/matplotlibrc` 文件。根據實際情況修改，找到如下兩項，去掉前面的 `#`，並在 `font.sans-serif` 冒號後面加上 `SimHei`，保存退出。

```
font.family         : sans-serif       
font.sans-serif     : SimHei, Bitstream Vera Sans, Lucida Grande,Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```

```py
# 變更中文字型
plt.rcParams['font.sans-serif'] = ['simhei']

# 修復負號顯示問題 (思源黑體可以正常顯示負號，所以不需要加這行)
plt.rcParams['axes.unicode_minus'] = False
```

Method 2: 直接指定字體檔案

```py
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 設定字體的檔案位置，並放到fm.FontProperties裡
fontPath = r'C:\Users\user\Downloads\NotoSansMonoCJKtc-Bold.otf'
font30 = fm.FontProperties(fname=fontPath, size=30)
plt.xticks(x, x_labels, fontproperties=font30)
```

## 找到中文的字體檔 (ttf/otf)

只要你matplotlib中的字體資料夾中沒有simhei字體，則這招就會失效。這篇文章主要分享如何自行新增字體來解決matplotlib在python中顯示中文的方法。

1. 將字體放到matplotlib的字體套件資料夾

    ```py
    import matplotlib
    print(matplotlib.__file__)
    ```

2. 到 `~/.matplotlib/` 刪除所有快取檔案
3. 重新 `import matplotlib`，並查看 `~/.matplotlib/fontList.json` 檔案

```py
# matplotlib不會每次啓動時都重新掃描所有的字體文件並創建字體索引列表，
# 因此在複製完字體文件之後，需要運行下面的語句以重新創建字體索引列表
import matplotlib as mpl
from matplotlib.font_manager import _rebuild
_rebuild()
```
