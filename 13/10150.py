from ipaddress import ip_network

for mask in range (0 , 33):
    net = ip_network(f'145.192.94.230/{mask}', 0)
    print(net, net.netmask)