from ipaddress import *

ip1 = ip_address("112.117.107.70")
ip2 = ip_address("112.117.121.80")

for mask in range(16, 33):
    net1 = ip_network(f"{ip1}/{mask}", strict=False)
    net2 = ip_network(f"{ip2}/{mask}", strict=False)
    if net1 == net2:
        print(len(list(net1.hosts())))
        print(net1.num_addresses)