from ipaddress import *

def res(ip):
    sbin = f"{int(ip):032b}"
    return "101" not in sbin

q = 0
ip = ip_address("136.36.240.16")
mask = "255.255.255.248"
net = ip_network(f"{ip}/{mask}", 0)
for ips in net:
    if res(ips):
        q += 1
print(q)
