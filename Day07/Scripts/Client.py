import socket

if __name__ == '__main__':
    # 1、创建客户端套接字对象
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2、和服务器端套接字建立连接(参数必须是一个元祖)
    clientSocket.connect(("127.0.0.1", 8090))
    # 3、发送数据
    clientSocket.send('123'.encode(encoding='utf-8'))
    # 4、接收数据
    recv_data = clientSocket.recv(1024).decode('utf-8')
    print(recv_data)
    # 5、关闭客户端套接字
    clientSocket.close()