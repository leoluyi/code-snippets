package main

import (
  "log"
  "net"
  "net/rpc"
)

// 作為rpc的server func，必須接受兩個參數 (duck typing) (request string, reply *string)
// 另外返回值為error，必須為公開的方法

type HelloService struct{}

func (h *HelloService) Hello(request string, reply *string) error {
  *reply = "hello: " + request
  return nil
}

func main() {
  // rpc.Register會將object中所有滿足rpc規則的方法註冊為rpc函數
  // 所有註冊的方法會被放在HelloService服務空間下。
  rpc.RegisterName("HelloService", new(HelloService))

  // 建立聆聽一個tcp連線，
  listner, err := net.Listen("tcp", ":8080")
  if err != nil {
    log.Fatal(err)
  }
  for {
    conn, err := listner.Accept()
    if err != nil {
      log.Fatal(err)
    }

    // rpc.ServeConn在該連線上提供client rpc函數
    go rpc.ServeConn(conn)
  }
}
