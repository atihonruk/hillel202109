from socket import *
from time import sleep
from threading import Thread


HOST = '127.0.0.1'
PORT = 5555


_rec_count = 0


def counter():
    global _rec_count
    while True:
        sleep(1)
        print(_rec_count)
        _rec_count = 0


Thread(target=counter).start()


with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        sock.sendall(b'1')
        data = sock.recv(256)
        _rec_count += 1
