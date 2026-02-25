from ipaddress import ip_network


mask = "255.192.0.0"
net = f"191.128.66.83/{mask}"
ip = ip_network(net, 0)
print(ip)