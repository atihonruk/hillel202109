from socket import *
from threading import Thread
from concurrent.futures import ProcessPoolExecutor  # ThreadPoolExecutor


HOST = '127.0.0.1'  # '0.0.0.0'
PORT = 5555

process_pool = ProcessPoolExecutor(4)


# 1, 1, 2, 3, 5, 8 
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

def fib_handler(client, addr):
    with client:
        while True:
            data = client.recv(256)
            if not data:
                break
            n = int(data)
            fut = process_pool.submit(fib, n)
            res = fut.result()
            client.sendall((str(res) + '\n').encode())


def echo_handler(client, addr):
    with client:
        while True:
            data = client.recv(256) # waiting for data
            if not data:
                break
            client.sendall(data)


def start_server(handler):
    # with socket(AF_INET, SOCK_STREAM) as sock:  # IPv4
    with create_server((HOST, PORT)) as sock:  # Python 3.8+
        # sock.bind((HOST, PORT))
        # sock.listen() # backlog
        print(f'Listening on {HOST}:{PORT}')
        while True:
            client, addr = sock.accept()  # waiting for connection
            host, port = addr
            print(f'Connected from {host}:{port}')
            # handle_connection(client, addr)
            Thread(target=handler, args=(client, addr)).start()

# GIL

if __name__ == '__main__':
    start_server(fib_handler)
