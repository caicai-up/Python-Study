import socket

class WebServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口和IP
        self.server.bind(('', 8090))
        # 设置监听
        self.server.listen(128)

    def handle(self, newSocket, addr):
        recvData = newSocket.recv(1024)
        recvData = recvData.decode('utf-8')
        print(f"Received: {addr} : {recvData}")
        newSocket.send("code : 200".encode("utf-8"))
        newSocket.close()

    def start(self):
        print("Server started...")
        while True:
            conn, addr = self.server.accept()
            self.handle(conn, addr)


if __name__ == "__main__":
    webServer = WebServer()
    webServer.start()
