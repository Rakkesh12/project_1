"""import os ,ipaddress
while True:
    ip=input("enter the ip address")
    try:
        print(ipaddress.ip_address(ip))#it will check weather the ip is valid or not valid
        print("ip valid")
    except:
        print("ip not valid")
    finally:
        print("bhuvanesh")
        if ip=="mango":
            print("mango")
            break"""
#import os
#print(os.system("ipconfig"))#for getting the ip config details configuration in python

import socket
raki_1=socket.socket()
print("socket is successfully created")
port=40647
raki_1.bind('',port)
print("socket binded to %s"%(port))
raki_1.listen(5)
print("socket listening")
while True:
    c,address=raki_1.accept()
    print("got connection",address)
    c.send(b'thank you for connecting')

