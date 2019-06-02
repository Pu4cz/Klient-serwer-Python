from socketserver import ThreadingTCPServer, BaseRequestHandler,socket
from threading import Thread
import pickle,time,datetime,os
import hashlib

messages = []
temp = []
os.system("cls")
class Echo(BaseRequestHandler):


    def handle(self):
        self.temp = []
        Thread(target=self.send).start()

        self.password = self.request.recv(8192)
        self.password = self.password.decode()
        print(self.password)
        print('/n',hex_dig)

        if self.password != hex_dig:
            self.answer = 'False'
            self.request.send(self.answer.encode())
        else:
            self.answer = 'True'
            self.request.send(self.answer.encode())
            self.username = self.request.recv(8192)
            self.username = self.username.decode()
            print("Got connection from {}:{}".format(self.client_address[0],
                                                     self.client_address[1]))




        while True:
            msg = self.request.recv(8192)
            msg = "[{} {}]: {}".format(datetime.datetime.now().strftime("%H:%M:%S"),
                               self.username,
                               msg.decode())

            messages.append(msg)
            print(msg)



            if not msg:
                break


    def send(self):

        global temp, messages
        while 1:


            if len(self.temp) != len(messages):

                data_string = pickle.dumps(messages)
                self.request.send(data_string)
                self.temp = [item for item in messages]
if __name__ == "__main__":

    serv = ThreadingTCPServer(("",20000), Echo)
    password = input("input server password: ")
    hash_pass = hashlib.sha512(bytes(password,'utf-8'))
    hex_dig = hash_pass.hexdigest()
    serv.serve_forever()