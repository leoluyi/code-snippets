package main

import (
  "fmt"
  "log"
  "net/rpc"
)

func main() {
  // rpc.Dial 連接該rpc服務
  conn, err := rpc.Dial("tcp", ":8080")
  if err != nil {
    log.Fatal(err)
  }

  var reply string
  // 透過conn.Call來使用rpc方法。
  // conn.Call(serviceMethod, args, reply)
  conn.Call("HelloService.Hello", "Jack", &reply)
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(reply)
}
