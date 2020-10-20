# import socket
# import json
# #import CarMove
# import threading
#
# class CarControl():
#     def __init__(self):
#         self.s=socket.socket()
#         self.s.connect(("192.168.100.163",7654))
#         self.s.send({"msg":"Hello, I'm a car"})
#         print(self.s.recv(1024).decode())
#         #self.car=CarMove()
#     def recevice(self):
#         while True:
#             data=self.s.recv(1024)
#             data=data.decode()
#             data=self.toDic(data)
#             a=self.findmove(data)
#             self.car.move(int(a[0],int(a[1],int(a[2]),int(a[4]))))
#
#
#     def func(self):
#         thread=threading.Thread(args=self.func1,)
#         thread.start()
#
#     def func1(self):
#         for i in range(100):
#             print(i)
#
#     """
#         把json格式转化为字典格式（转化为的字典类型的数据必须包含key：msg）
#         data：json格式数据
#         return:返回字典类型
#     """
#
#     def toDic(self,data):
#         dataToDic = json.loads(data)
#         return dataToDic
#
#     def findmove(self,str):
#         str = str.split("移动")[1]
#         left01 = str.split(",")[0]
#         left02 = str.split(",")[1]
#         right01 = str.split(",")[2]
#         right02 = str.split(",")[3]
#         return (left01, left02, right01, right02)
#
# if __name__=="__main__":
#     carControl=CarControl()
#     carControl.func()
#
#
#
import socket
import json
from CarMove import CarMove
import threading


class CarControl():
    def __init__(self):
        self.s = socket.socket()
        self.s.connect(("192.168.1.110", 7654))
        self.s.send('{"code":2000,"msg":"Car"}'.encode())
        print(self.s.recv(1024).decode())
        self.car = CarMove()

    def recevice(self):
        while True:
            data = self.s.recv(1024)
            print(data.decode())
            if data.decode()[len(data.decode()) - 1] == "}" and len(data.decode())<70:
                print("data", self.toDic(data.decode())["msg"])
                self.car.move(self.toDic(data.decode())["msg"])
            
            # print(111)
            # data = self.toDic(data)
            # a = self.findmove(data)
            #self.car.
    def func1(self):
        while True:
            print(self.s)

    def start(self):
        thread = threading.Thread(target=self.recevice,)
        thread.setDaemon(True)
        thread.start()

    """
        把json格式转化为字典格式（转化为的字典类型的数据必须包含key：msg）
        data：json格式数据
        return:返回字典类型
    """

    def toDic(self, data):
        dataToDic = json.loads(data)
        return dataToDic

    def findmove(self, str):
        str = str["msg"]
        str = str.split("\u79fb\u52a8")[1]
        print("str", str)
        str = str.split(",")

        left01 = str[0]
        left02 = str[1]
        right01 = str[2]
        right02 = str[3]
        return (left01, left02, right01, right02)


if __name__ == "__main__":
    carControl = CarControl()
    carControl.start()