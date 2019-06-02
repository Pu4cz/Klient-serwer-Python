import socket,pickle,os
from threading import Thread
import time
import hashlib
s = socket.socket()
s.connect(('localhost',20000))
password = input("Enter chatroom password: ")
hash_pass = hashlib.sha512(bytes(password,'utf-8'))
hex_dig = hash_pass.hexdigest()
s.send(hex_dig.encode())

ans = s.recv(8192).decode()

print(ans)
if ans == 'False':
    print("sorry wrong password")
    exit()
if ans == 'True':
    pass
def receive():

    while True:
        data = s.recv(8192)
        data = pickle.loads(data)
        os.system('CLS')
        for item in data:
            print(item)


username = input("Enter your username: ")





Thread(target=receive).start()

s.send(username.encode())
time.sleep(0.1)
while True:

    msg = input(">>")

    if not msg:
        break
    s.send(msg.encode())
    time.sleep(0.1)