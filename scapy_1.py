import scapy.all as scapy
#request=scapy.ARP()
#print(request.summary())
from scapy.all import*
ip=Ether()
print(ip)
print(ip.show())
#in etherenet what is farme
#frame are used for data transmission it is used in datalink layer
#etherent-all data transfer:frames:frame number/frame length
myframe=Ether() /IP()/TCP()/APIs()
print(myframe)
print(myframe.show())

s=IP(dst='google.com')/ICMP()
print(s)