#! /usr/bin/env python2.7

# -#- coding: utf-8 -#-
# vim:fenc=utf-8
# read.py
# Copyright (C) 2019 Jecsan Blanco <jblancolicano1@buffs.wtamu.edu>
# Distributed under terms of the MIT license.
from scapy.all import *
def main():
    packets = packets = rdpcap('Week5.pcap')
    data = ""
    for packet in packets:
        query = str(packet[DNSQR].qname)
        if 'fakedns' in query:
            data += query.split('.')[0]

    newFile = open("image.dump", "wb")
    newFile.write(data)

    newFile = open("image.png", "wb")
    newFileByteArray = bytearray(data)
    newFile.write(newFileByteArray)

    return
# end main

if __name__ == "__main__":
    main()
