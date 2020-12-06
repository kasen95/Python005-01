
import socket

'''
题目：不使用开源框架，基于 TCP 协议改造 echo 服务端和客户端代码，实现服务端和客户端可以传输单个文件的功能。
'''

host = '127.0.0.1'
port = 8073

'''
客户端
1.获取用户内容
2.把内容已socket发到服务端
'''
class client():

    def run(self):
        # 建立socket连接
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        s.connect((host, port))

        # 获取用户输入内容
        while True:
            content = input('请输入命令：').encode('utf-8')
            if not content:
                break
            s.send(content)
            result = s.recv(1024).decode('utf-8')
            print(result)

        # 关闭socket连接
        s.close()

if __name__ == "__main__":
    client().run()


