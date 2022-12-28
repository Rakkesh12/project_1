import psutil
import time
import os
import pandas as pd
UPDATE_DELAY=1
def get_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes<1024:
            return f"{bytes:2f}{unit}B"
        bytes/=1024
        io=psutil.net_io_counters(pernic=True)
        #bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv
while True:
    time.sleep(UPDATE_DELAY)
    io_2=psutil.net_io_counters(pernic=True)
    data=[]
    for iface,iface_io in io.items():
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f"upload:{get_size(io_2.bytes_sent)}"
    f",download:{get_size(io_2.bytes_recv)}"
    f",upload Speed:{get_size(us/UPDATE_DELAY)}/s"
    f",Download speed:{get_size(ds/UPDATE_DELAY)}/s",end="\r")
    bytes_sent,bytes_recv=io_2.bytes_sent,io_2.bytes_recv
