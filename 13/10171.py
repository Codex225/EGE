from ipaddress import *
ip = ip_address('115.53.128.88')
ip_net = ip_address('115.53.128.0')
for mask in range(16, 33):
    q = 0
    net = ip_network(f'{ip}/{mask}', 0)
    #print(net[0])
    for address in net:
        q += 1
    #if net[0] == ip_net and net.num_addresses >= 1002:

    if net[0] == ip_net and q >= 1002:
        print(mask)
        # q = 0
        # for host in net:
        #     q += 1
        #     if q >1002:
        #         print(mask)