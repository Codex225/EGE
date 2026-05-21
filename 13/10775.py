from ipaddress import *

net = ip_network("156.128.0.227/255.255.255.248", 0)
ip = ip_address("156.128.0.227")

q = 0
for host in net.hosts():
    q += 1
    if host == ip:
        print(q)
        break