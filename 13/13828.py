from ipaddress import *
ip = ip_address("192.168.32.48")
mask = "255.255.255.192"
net = ip_network(f"{ip}/{mask}", 0)
q = 0
for ips in net:
    if ip in net.hosts() and (f'{int(ips):032b}').count("1") % 5 != 0:
        q += 1
print(q)