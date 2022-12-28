from netmiko import ConnectHandler
CSR={
    "device_type":"cisco_nxos",
    #"ip":"Sandbox-iosxe-latest-1.Cisco.com",
    "ip":" sandbox-iosxe-recomm-1.cisco.com",
    "port":22,
    "username":"developer",
    "password":"C1sco12345"
}

net_connect=ConnectHandler(**CSR)
output=net_connect.send_command('show ip int brief')#it will give all the network interfaces present in the router
output_1=net_connect.send_command('show clock')
#print(output_1)
print(output)
output_3=net_connect.send_command("show run")
#print(output_3)
net_connect.disconnect()#to close the connection we use disconnect

#output_runhost = net_connect.send_command('show run'| 'i host')
#print(output_runhost)

"""CSR1000v Host: sandbox-iosxe-latest-1.cisco.com
SSH Port: 22
NETCONF Port: 830
gRPC Telemetry Port: 57500
RESTCONF Port: 443 (HTTPS)
Username: developer
Password: C1sco12345"""