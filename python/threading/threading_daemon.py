"""
join():

主線程 A 中創建了子線程 B，並且在主線程 A 中調用了 `B.join()`，
它的含義是「將線程 B 加入到當前線程的執行流程中」，
也就是說主線程 A 會在調用的地方等待，直到子線程 B 完成操作或超時後才可以接著往下執行。

另外，`join` 可以設置超時時間，在超時後繼續執行當前線程，停止阻塞，
意味著「B 線程從當前執行流程中（A 線程）再次獨立出來，不受主線程影響」。
"""

import time
import threading


def sub_thread_fun():
    print("sub thread start")
    while True:
        time.sleep(1)
        print("sub is alive")
    print("sub thread end")


try:
    print("main thread start")
    t1 = threading.Thread(target=sub_thread_fun, args=())

    # 當同時使用 setDaemon(True) 方法和 join() 方法時，可以實現：
    # 主線程給子線程足夠的時間去完成任務，
    # 也能在主線程退出時讓子線程也結束，能更好的控制子線程的行為。

    t1.setDaemon(True)
    t1.start()
    t1.join(3)
    t1.join(3)
    t1.join(3)  # 多次join無影響,但如果加入時間參數，將是等待多個時間參數之和
    time.sleep(3)
    print("main thread end")
    print("sub thread is alive ? {0}".format(t1.is_alive()))
except KeyboardInterrupt as e:
    print(e)
    print("exit")
