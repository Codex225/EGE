from ipaddress import *
ip = ip_address("225.200.110.15")
mask = "255.255.248.0"
net = ip_network(f"{ip}/{mask}", strict=False)
print(list(net.hosts())[-1])