from ipaddress import *

ip1 = ip_address("157.127.172.56")
ip2 = ip_address("157.127.191.78")

for mask in range(16, 33):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1.network_address != net2.network_address:
        print(mask)