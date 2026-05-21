from ipaddress import *
net = ip_network("171.128.0.0/255.128.0.0")
ip0 = ip_address("171.128.0.0")

def res(ip):
    sbin = f"{int(ip):032b}"
    return sbin[:16].count("1") < sbin[16:].count("1")

q = 0
for ips in net:
    if res(ips):
        q += 1
print(q)

