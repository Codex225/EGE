from ipaddress import ip_network

for mask in range(1, 33):

    net = ip_network(f"115.12.69.38/{str(mask)}", 0)
    print(net)