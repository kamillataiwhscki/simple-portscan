from scapy.all import *

hostname = "google.com.br"

pkt, unans = sr(IP(dst=hostname, ttl=(0,14))/ TCP())

for sr,rcv in pkt:
  print (sr.ttl, rcv.src)
