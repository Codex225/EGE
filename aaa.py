from ipaddress import ip_network

net = ip_network("192.168.1.0/24")
for address in net:
    ds = int(address)
    print(ds, type(ds))
print(net)