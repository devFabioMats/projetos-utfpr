#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import time
import threading
import select
import traceback

class Server(threading.Thread):
    def initialise(self, receive):
        self.receive = receive

    def run(self):
        lis = []
        lis.append(self.receive)
        while 1:
            read, write, err = select.select(lis, [], [])
            for item in read:
                try:
                    s = item.recv(1024)
                    if s != b'':
                        chunk = s
                        print(chunk.decode() + '\n>>')
                except:
                    traceback.print_exc(file=sys.stdout)
                    break


class Client(threading.Thread):
    def connect(self, host, port):
        self.sock.connect((host, port))

    def client(self, host, port, msg):
        sent = self.sock.send(msg)

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            host = input("Digite o IP do servidor \n>>")
            port = int(input("Digite a porta do servidor\n>>"))
        except EOFError:
            print("Erro")
            return 1

        print("Conectando...")
        self.connect(host, port)
        print("Conectado!")
        user_name = input("Digite seu nome de usuário\n>>")
        receive = self.sock
        time.sleep(1)
        srv = Server()
        srv.initialise(receive)
        srv.daemon = True
        print("Iniciando serviço de recebimento")
        srv.start()
        while 1:
            msg = input('>>')
            if msg == 'exit':
                break
            if msg == '':
                continue
            msg = user_name + ': ' + msg
            data = msg.encode()
            self.client(host, port, data)
        return (1)


if __name__ == '__main__':
    print("Iniciando cliente")
    cli = Client()
    cli.start()