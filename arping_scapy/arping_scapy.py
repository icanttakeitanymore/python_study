#!/usr/bin/env python3
from scapy.all import srp,Ether,ARP, conf
import sys

def arping(network):
    iprange=network
    conf.verb=2
    ans,munans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=iprange),
                          timeout=2)
    collection = []
    for snd,rcv in ans:
        result = rcv.sprintf(r"%ARP.psrc% %Ether.src%").split()
        collection.append(result)
    return collection

if __name__ == '__main__':
    network = sys.argv[1]
    for i in arping(network):
        print('found: ',i)
