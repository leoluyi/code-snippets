
```
netstat -ntlp

-l, --listening
    Show only listening sockets.  (These are omitted by default.)
--numeric , -n
    Show numerical addresses instead of trying to determine symbolic host, port or user names.
--route , -r
    Display  the kernel routing tables. See the description in route(8) for details.  netstat -r and route -e
    produce the same output.
-p, --program
    Show the PID and name of the program to which each socket belongs.
```

列出使用中的網路連線

```
netstat -atnp | grep ESTA
```

查看本機服務 - `-lx` 參數可以列出目前 listening 的 UNIX 連接埠：

```
netstat -lx
```

### 用 awk 分析連線

分析 Apache 的連線，列出每個 IP 位址的連線數：

```
netstat -anpt | grep apache2 | grep ESTABLISHED | awk -F "[ :]*" '{print $4}' | uniq -c
```

將所有連線的 IP 位址列出來，並依照每個 IP 位址的連線數排序：

```
netstat -an | grep ESTABLISHED | awk '/^tcp/ {print $5}' | awk -F: '{print $1}' | sort | uniq -c | sort -nr

# 2 119.160.254.215
# 1 98.138.250.102
# 1 98.138.243.53
# 1 23.41.139.27
# 1 124.108.101.11
# 1 116.214.12.74
# 1 106.10.170.120
```

將所有連線的 IP 位址列出來，用 + 號表示連線數：

```
netstat -an | grep ESTABLISHED | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq -c | awk '{ printf("%st%st",$2,$1) ; for (i = 0; i < $1; i++) {printf("+")}; print "" }'
```

