from ipaddress import ip_network, ip_address

net = ip_network("156.132.15.138/255.255.252.0", 0)
ip = ip_address("156.132.15.138")
n = 0
for ips in net:
    if ip == ips:
        print(n, ips)
    n += 1