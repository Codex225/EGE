from ipaddress import *


for mask in range(24, 33):
    net = ip_network(f"172.16.168.0/{mask}", strict=False)
    q = 0
    for ips in net:
        if f"{int(ips):032b}".count("0") % 7 == 0:
            q += 1
    if q == 35:
        print(net.netmask)