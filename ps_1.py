import pandas as pd
import psutil
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear',shell=True)
remoteServer=input("enter a remote host")
remoteServerIp=socket.gethostbyname(remoteServer)
print("please wait ,scanning remote host",remoteServerIp)
t1=datetime.now()
try:
    for port in range(1,500):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect((remoteServerIp,port))
        if result==0:
            print("port{}".format((port)))
            sock.close()
except KeyboardInterrupt:
    print("you pressed")
    sys.exit()
except socket.gaierror:
    print("hostname")
    sys.exit()
except socket.error:
    print("could not connect")
    sys.exit()

#import pandas
"""li=["bytes_sent",'bytes_recv','packet_sent',"packet_recv","errin","errout","dropin","dropout"]
result_5=psutil.net_io_counters(pernic=True)
arr=pd.DataFrame(result_5,index=li)
print(arr)
result_5=psutil.net_io_counters(pernic=False)
bytes_1=getattr(result_5,'packets_recv')
print("packets_received {}".format(bytes_1))
print(result_5)"""