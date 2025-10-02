#! /usr/bin/env python

import socket
import sys
import time
import threading
import select
import traceback
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# AESGCM.generate_key(bit_length=128)
# nonce = os.urandom(12)
key = b'A\xe0 9.\xd6\x1cNY\xba\xf7\x08d\xa9To'
nonce = b'\x95\xa4\xad#\xceg\xbd\x02w\x8cf\x05'
aesgcm = AESGCM(key)
aad = b"autenticado"

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
                    if s != '':
                        chunk = s
                        chunk = aesgcm.decrypt(nonce, chunk, aad)
                        print(chunk.decode() + '\n>>')
                except:
                    traceback.print_exc(file=sys.stdout)
                    break


class Client(threading.Thread):
    def connect(self, host, port):
        self.sock.connect((host, port))

    def client(self, host, port, msg):
        sent = self.sock.send(msg)
        # print "Sent\n"

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            host = input("Enter the server IP \n>>")
            port = int(input("Enter the server Destination Port\n>>"))
        except EOFError:
            print("Error")
            return 1

        print("Connecting\n")
        s = ''
        self.connect(host, port)
        print("Connected\n")
        user_name = input("Enter the User Name to be Used\n>>")
        receive = self.sock
        time.sleep(1)
        srv = Server()
        srv.initialise(receive)
        srv.daemon = True
        print("Starting service")
        srv.start()
        while 1:
            msg = input('>>')
            if msg == 'exit':
                break
            if msg == '':
                continue
            msg = user_name + ': ' + msg
            data = msg.encode()
            data = aesgcm.encrypt(nonce, data, aad)
            self.client(host, port, data)
        return (1)


if __name__ == '__main__':
    print("Starting client")
    cli = Client()
    cli.start()