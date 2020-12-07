import socket
import struct
import re


def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network + " " + netmask
	
	



s = editor.getText()
 

s = re.sub(r'^[0-9./]', r'', s)

sArray = s.splitlines()

linelist = []

 

out = ""
count = 0

for line in sArray:
	print(line)
	tmp = cidr_to_netmask(line)
	print(tmp)