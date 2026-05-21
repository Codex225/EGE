from ipaddress import *
q = 0
for o4 in range(0, 256):
    net = ip_network(f"246.81.65.{o4}/255.255.255.224", 0)
    ip_a = ip_address(f"246.81.65.{o4}")
    if all(f"{int(ip):032b}"[16:24].count("0") > f"{int(ip):032b}"[24:].count("0") for ip in net.hosts()):
        if net[0] < ip_a < net[-1]:

            q += 1

print(q)