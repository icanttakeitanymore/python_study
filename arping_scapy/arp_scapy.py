#!/usr/bin/env python3
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import Ether,ARP,srp,conf
import sys
def get_arp(ip):
    conf.verb = 0
    ans,unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip),timeout=2)
    for snd,rcv in ans:
        print('sending packet: ',snd.sprintf(r"%Ether.dst% %ARP.pdst%"),
              '\n'
              ,'\breceived packet:',rcv.sprintf(r"%ARP.psrc% %Ether.src%"))
if __name__ == '__main__':
    ip = sys.argv[1]
    get_arp(ip)
