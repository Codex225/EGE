from ipaddress import *

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for mask in range (1, 33):
    net1 = ip_network(f"{ip1}/{mask}", 0)
    net2 = ip_network(f"{ip2}/{mask}", 0)
    if net1[0] != net2[0]:
        print(mask)