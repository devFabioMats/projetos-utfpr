#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import traceback
import threading
import select

SOCKET_LIST = []
TO_BE_SENT = []
SENT_BY = {}

class Server(threading.Thread):
    def init(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.bind(('', 50250))
        self.sock.listen(2)
        SOCKET_LIST.append(self.sock)
        print("Servidor iniciado na porta 50250")

    def run(self):
        while 1:
            read, write, err = select.select(SOCKET_LIST, [], [], 0)
            for sock in read:
                if sock == self.sock:
                    sockfd, addr = self.sock.accept()
                    print(f"Cliente conectado de {addr}")
                    SOCKET_LIST.append(sockfd)
                else:
                    try:
                        s = sock.recv(1024)
                        if s == b'':
                            print(f"Cliente {sock.getpeername()} desconectou")
                            SOCKET_LIST.remove(sock)
                            sock.close()
                            continue
                        else:
                            TO_BE_SENT.append(s)
                            SENT_BY[s] = str(sock.getpeername())
                            print(f"Mensagem recebida de {sock.getpeername()}: {s.decode()}")
                    except:
                        print(f"Erro com cliente {sock.getpeername()}")
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        sock.close()


class handle_connections(threading.Thread):
    def run(self):
        while 1:
            read, write, err = select.select([], SOCKET_LIST, [], 0)
            for items in TO_BE_SENT:
                for s in write:
                    try:
                        if (str(s.getpeername()) == SENT_BY[items]):
                            print(f"Ignorando envio para remetente {s.getpeername()}")
                            continue
                        print(f"Enviando para {s.getpeername()}")
                        s.send(items)
                    except:
                        traceback.print_exc(file=sys.stdout)
                        if s in SOCKET_LIST:
                            SOCKET_LIST.remove(s)
                        s.close()
                TO_BE_SENT.remove(items)
                del (SENT_BY[items])


if __name__ == '__main__':
    srv = Server()
    srv.init()
    srv.start()
    print("Lista de sockets:", SOCKET_LIST)
    handle = handle_connections()
    handle.start()
