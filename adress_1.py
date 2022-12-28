import ifaddr
adapaters=ifaddr.get_adapters()
for adapater in adapaters:
    print("ip of network adapter"+adapater.name)
    for ip in adapater.ips:
        print("%s %s" %(ip.ip,ip.network_prefix))