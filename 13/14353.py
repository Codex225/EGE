from ipaddress import *

ip0 = ip_address("192.168.72.128")
mask = "255.255.255.128"

def c1(ip):
    return (f"{int(ip):032b}").count("1") % 10 == 0
q = 0
for ip in ip_network(f"{ip0}/{mask}", strict=False):
    if c1(ip):
        q += 1
print(q)