'''
1.建立socket服务连接监听
2.接收tcp连接
3.调起系统cmd服务执行命令
4.把cmd服务执行结果处理并返回
5.关闭tcp连接
6.关闭socket服务监听
'''
import os
import socket

from week02 import echo_client


class server():

    def run(self):
        tcp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        tcp_server.bind((echo_client.host,int(echo_client.port)))
        tcp_server.listen(5)

        while True:
            s, address = tcp_server.accept()
            print('接收到请求{}，地址{}'.format(s, address))

            while True:
                content = s.recv(1024).decode('utf-8')
                print('接收到的内容:{}'.format(content))
                if not content:
                    break

                cmd = os.popen(content)
                cmd_result = cmd.read()
                cmd_status=cmd.close()

                print('执行码：{}'.format(str(cmd_status)))

                #执行成功，返回码为None
                if not cmd_status:
                    s.send(bytes(cmd_result.encode('utf-8')))
                else:
                    s.send(b'error!')

            s.close()


if __name__ == "__main__":
    server().run()