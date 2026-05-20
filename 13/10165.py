from ipaddress import *
net = ip_network("192.168.0.0/255.255.255.128")


q = 0
for host in net:
    q += 1
print(q)