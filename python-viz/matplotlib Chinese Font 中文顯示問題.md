# matplotlib 中文顯示問題

- https://daxpowerbi.com/如何在win-10解決matplotlib中文顯示的問題/
- https://medium.com/@aitmr1234567890/解決python-3-matplotlib與seaborn視覺化套件中文顯示問題-f7b3773a889b
- https://zhuanlan.zhihu.com/p/38544714

## TL;DR

1. 安裝 otf 中文字體

安裝中文字體檔 (ttf/otf)，或將字體檔丟到 matplotlib 的安裝位置 `site-packages/matplotlib/mpl-data/fonts/ttf`，這裡建議直接安裝 [Google Noto Fonts](https://www.google.com/get/noto/#sans-hant)

> macOS 中的字體格式是 ttc (Windows 系統字型「微軟正黑體」為 `msjh.ttc`)，但 matplotlib 字型資料夾的檔案型態只能接受 ttf/otf 格式。需要下載 ttf 類中文字體，再安裝到 macOS 上 (不用另外將字體放到套件資料夾)。
> 
> --> 下載 ttf 格式的 [微軟正黑體](http://cloud.ziti8.cn/fonts/weiruan/%E5%BE%AE%E8%BD%AF%E6%AD%A3%E9%BB%91%E4%BD%93.ttf)

```py
# 找出 matplotlib 的安裝位置
import matplotlib
print(matplotlib.__path__)
```

2. 刪除快取檔案 `~/.matplotlib/fontList.json`，並手動重新建立字型索引

```py
# matplotlib 不會每次啓動時都會自動重新掃描所有的字體文件並創建字體索引列表，
# 因此在複製完字體文件之後，需要運行下面的語句以重新創建字體索引列表
from matplotlib.font_manager import _rebuild
_rebuild()
```

查看 `~/.matplotlib/fontList.json` 檔案是否有安裝的中文字型

```
{
    "fname": "/Users/leoluyi/Library/Fonts/jf-jinxuan-medium.otf",
    "name": "jf-jinxuan-fresh",  # 確認字型名字
    ...
}
```

3. Set font family

```py
import matplotlib.pyplot as plt
# 變更中文字型
plt.rcParams['font.sans-serif'] = ['jf-jinxuan-fresh', 'Noto Sans CJK TC']
# 修復負號顯示問題 (思源黑體可以正常顯示負號，所以不需要加這行)
plt.rcParams['axes.unicode_minus'] = False

x_labels = ['小', '中', '大']
x = list(range(len(x_labels)))
y = [-3, 0, 3]
# 在plt.xticks中，加入fontproperties=myfont參數
plt.scatter(x, y)
plt.xticks(x, x_labels)
plt.title('獲救情況 (1為獲救)') # 標題
plt.show()
```

4. (Optional) 直接在 `matplotlibrc` 修改就不用另外指定 `plt.rcParams`

修改 `~/.matplotlib/matplotlibrc` 加入下面幾行

- Linux: `~/.config/matplotlib/matplotlibrc`
- Mac/Windows: `~/.matplotlib/matplotlibrc`

```
# ~/.matplotlib/matplotlibrc
font.family         : sans-serif
font.sans-serif     : jf-jinxuan-fresh, Noto Sans CJK TC, Bitstream Vera Sans, Lucida Grande,Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
```

> 也可以（但不建議）修改 matplotlib 安裝路徑中的 `site-packages/matplotlib/mpl-data/matplotlibrc` 文件 (因為重新安裝後設定便會消失)，找到如下兩項，去掉前面的 `#`，並在 `font.sans-serif` 冒號後面加上 `Noto Sans CJK TC`，保存退出。(解決負號 '-' 顯示為方塊的問題：找到 `axes.unicode_minus`，將 `True` 改為 `False`

## Solution 2: 每次手動指定字體絕對路徑

```py
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 設定字體的檔案位置，並放到fm.FontProperties裡
font_path = 'C:/Users/user/Downloads/NotoSansMonoCJKtc-Bold.otf'  # Windows
font_path = '/System/Library/Fonts/STHeiti Medium.ttc'  # Mac
myfont = fm.FontProperties(fname=font_path)

# 加入 fontproperties=myfont 參數
plt.plot((1, 2, 3), (4, 3, 1)) 
plt.title("聲量圖", fontproperties=myfont) 
plt.ylabel("文章數量", fontproperties=myfont) 
plt.xlabel("時間", fontproperties=myfont)  
plt.show()
```

## Misc

Find the path of matplotlib default font:

```python
from matplotlib.font_manager import findfont, FontProperties  
findfont(FontProperties(family=FontProperties().get_family()))
```

result:

```
site-packages/matplotlib/mpl-data/fonts/ttf
```
