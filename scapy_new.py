from scapy.all import*
a=IP(ttl=10)
print(a)
print(a.dst)

#a.dst='10.10.10.1'
a.dst='google.co.in'
print(a)
print(a.src)

c=IP()/TCP()
print(c.show())
d=Ether()/IP()/TCP()
print(d.show())
e=IP()/TCP()/'GET/HTTP/1.0\r\n\r\n'
print(e.show())
k=a=Ether()/IP(dst='www.google.co.in')/TCP()/'GET/raki.html HTTP/1.0\r\n\r\n'
print(k)
j=a=Ether()/IP(dst='www.google.co.in')/TCP()/'GET/index.html FTP/1.0\r\n\r\n'
print(hexdump(j))

k=IP(dst='google.co.in')
dst=