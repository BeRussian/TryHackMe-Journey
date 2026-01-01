## Cheet-Sheet for Tcpdump

## Basic capture

```bash
#Capture an all interfaces
tcpdump 
# Listen on spesific interface
tcpdump -i eth0

# Saved live captured packets into a file
tcpdump -i eth0 -w Packets.pcap

# Limit the number of packets captured
# Example capture 3000 packets to a Packets.pcap file -->
tcpdump -i eth0 -w Packets.pcap -c 3000

# Read packets from a file
tcpdump -r Packets.pcap

# dont convert known ip address to domain
tcpdump -n
# dont convert ip to domain and port to service(80 to http)
tcpdump -nn

# Verbose 
tcpdump -v
tcpdump -vv
tcpdump -vvv
```

## Adittional flags
```bash
# Quick output
-q

#Print MAC address header
-e

# Show packet data in ASCII
-A

# show packet data in hex
-xx

# show packet data in hex & ASCII
-X
```
## Basic Filtering
```bash
#Save only packet involving spesific $IP
tcpdump host $HOST/$IP -w http.pcap

#Filter by port
tcpdump port $PORT 
tcpdump src port $PORT
tcpdump dst port $PORT

# Filter by protocol
tcpdump icmp
#Optional protocols: ip,ip6,udp,tcp,icmp

* Use logical operators
# and / or / not
```

## Advanced filtering

```bash
# Show only packets that have length >=$LEN
tcpdump -r FILE greater $LEN
# Show only packets that have length <=$LEN
tcpdump -r FILE less $LEN
```
* We can filter packets by there header
* use the `protocol[startOffset:length(bytes -1/2/4)]` format
* length is not required
```bash
ether[0] & 1 != 0
# meaning we'll only see packets sent to multicast address 


ip[0] & 0xf != 5
# This means only show ip packets with addtional options 
# can indicate a malicous packet created by an attacker
```

```bash
#Show packets with only syn
tcpdunp "tcp[tcpflags] == tcp-syn"

#Show packets with at least a syn(can be also syn-ack)
tcpdump "tcp[tcpflags] & tcp-syn != 0"

#Show packets with at least syn or ack flags
tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) !=0"
```
