from ipaddress import *

ip = ip_address("151.192.0.0")
mask = "255.224.0.0"

def c1(ip):
    s = str(ip).split(".")
    q = 0
    for x in s:
        q += bin(int(x))[2:].count("1")
    return q == 16

q = 0
net = ip_network(f"{ip}/{mask}", strict=False)

for ips in net:
    if c1(ips):
        q += 1
print(q)