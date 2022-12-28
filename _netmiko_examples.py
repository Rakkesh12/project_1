from netmiko import ConnectHandler

with open('devices.txt') as routers:
    Router={
        "device_type":"cisco_ios",
        "ip":"Sandbox-iosxe-latest-1.Cisco.com",
        #"ip": "Sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345"
        }
    net_connect = ConnectHandler(**Router)
hostname=net_connect.send_command('show run|i host')
hostname.split(" ")
hostname,device,*rest=hostname.split(" ")
print("Backing up"+device)
filename="C:/Users/user685/PycharmProjects/pythonProject/new/raki.txt"

showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,'a')
log_file.write(showrun)
log_file.write(showvlan)
log_file.write(showver)
net_connect.disconnect()