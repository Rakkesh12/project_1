#import sys
#print("use current version",sys.version)
import socket#socket-packagec
s2=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
#core package
#3rd party package-pip-python installer package
#ip_address=socket.gethostname()#it will give host name
#print(ip_address)
#print(socket.gethostbyname(ip_address))#it will give the particular host ip adress
"""import os
with open('ip_list.txt') as file_name:
    parking=file_name.read()
    parking=parking.splitlines()
    print("{parking}  \n")
for ip in parking:
    response= os.popen(f"ping {ip} ").read()
    if("Requested timed"or "unreachable") in response:
        print(response)
        f=open("info_output.txt1","a")
        f.write(str(ip)+'link is down'+'/n')
        f.close()
    else:
        print(response)
        f = open("info_output.txt1", "a")
        f.write(str(ip) + 'link is up' + '/n')
        f.close()
with open("ip_output.txt") as file:
    output=file.read()
    f.close()
    print(output)
with open("info_output.txt1",'w') as file:
    pass"""
