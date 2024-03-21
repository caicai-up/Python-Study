import socket


def handle_client(newSocket, addr):
    recvData = newSocket.recv(1024)
    recvData = recvData.decode('utf-8')
    print(f"Received: {addr} : {recvData}")
    newSocket.send("HTTP/1.1 200".encode("utf-8"))
    newSocket.close()


class WebServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口和IP
        self.server.bind(('localhost', 8090))
        # 设置监听
        self.server.listen(128)

    def start(self):
        print("Server started...")
        while True:
            conn, addr = self.server.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    webServer = WebServer()
    webServer.start()