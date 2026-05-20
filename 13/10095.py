from ipaddress import *
def sum1(ip):
    s = str(ip)
    s = s.split(".")
    s = "".join(s)
    s = bin(int(s))[2:]
    return s.count("1") % 2

ip = ip_address("192.168.32.160")
mask = "255.255.255.240"
q = 0
for ips in ip_network(f"{ip}/{mask}", 0):
    print(ips)
    if sum1(ips) == 0:
        q += 1
print(q)