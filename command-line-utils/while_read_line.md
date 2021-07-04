# while read line

http://benjr.tw/97517

如果要處理檔案可以使用下面  while 語法：

```shell
while read line; do
  statements
done < file
```

`while` 會依據指定的檔案內容每次讀取一行 (儲存在變數 `$line`) 等待處理。一直到檔案結束
下面範例讀取 `/etc/passwd` 檔案，並擷取部分資料出來。

每一次讀取一行的資料儲存在變數 `$line` , 接著使用 awk 來處理。`awk` 在執行時就會先把第一行的資料讀取進來等待處理，所以 `FS` (Fields splits) 的定義 (冒號 `:` 來作欄位的分隔) 必須透過 `BEGIN {}` 事前先定義好，`print` 列印出 `\t` (tab) 與 ​`$1` 第一欄的資料：

```bash
#!/bin/bash
while read line; do
  echo $line | awk 'BEGIN{FS=":"} !/^ *#/ {print "User:\t"$1}'
done < /etc/passwd
```

執行結果：

```
User: root
User: daemon
User: bin
User: sys
User: sync
User: games
...
```

相同的輸出結果，使用 `IFS` (Internal Field Separator) , 資料會依據 IFS 所定義的區隔符號將一行資料中的資料儲存成不同變數.

```bash
#!/bin/bash
while IFS=":" read -r f1 f2 f3 f4 f5 f6 f7; do
  echo "User:" $f1
done < /etc/passwd
```

執行結果同上面的範例.

```
User: root
User: daemon
User: bin
User: sys
User: sync
User: games
...
```

