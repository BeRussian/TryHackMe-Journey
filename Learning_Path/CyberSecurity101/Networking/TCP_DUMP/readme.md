
## Walkthrough of Tcpdump: The Basics room 


## Theory - What will we learn?
* Capture packets and save them to a file
* Set filters on captured packets
* Control how captured packets are displayed



### Basic live capture
* Capture live network
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

#### Q:What option can you add to your command to display addresses only in numeric format?  

#### A: `-n`

## Filtering
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
#### Q: How many packets in traffic.pcap use the ICMP protocol?
```bash
tcpdump -r traffic.pcap -n icmp | wc -l
```
#### A: `26`


#### Q: What is the IP address of the host that asked for the MAC address of 192.168.124.137? 
```bash
tcpdump -r traffic.pcap src host 192.168.124.137 | grep -i arp
#Output:
07:18:29.940776 ARP, Reply ip-192-168-124-137.ec2.internal is-at 52:54:00:23:60:2b (oui Unknown), length 28

#This  shows us the replay, lets find the request
tcpdump -r traffic.pcap | grep -i arp

#Output
07:18:29.940761 ARP, Request who-has ip-192-168-124-137.ec2.internal tell ip-192-168-124-148.ec2.internal

```
#### A: `192.168.124.148`

##
#### Q: What hostname (subdomain) appears in the first DNS query?
```bash
tcpdump -r traffic.pcap udp port 53 -c 1 -n
#Output
07:18:24.058626 IP 192.168.124.137.33672 > 192.168.124.1.53: 39913+ A? mirrors.rockylinux.org. (40)

```
#### A: `mirrors.rockylinux.org`

## Advance filters
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
# this takes the first byte of the ether header 
# and checks against binary value of 1 --> 0000 0001
# this means will only see packets where:
# ether protocol -> first byte -> xxxx xxx1
# x -> doesnt matter if 0 or 1
# In ether protocol the first byte indicates multicase/unicase
# meaning we'll only see multicast address 
```
* another example
```bash
ip[0] & 0xf != 5
# First byte in ip header indicates ipv4/6
# binary of 0xf --> 0000 1111
# binary of 5 -->   0000 0101
# for this to be True the ip header shulde be:
# xxxx 0101
# So well see all the ip packets that doent equal to this
# This means only show ip packets with addtional options 
# can indicate a malicous packet created by an attacker

```
* Filter by tcp flags (syn/syn-ack/ack)
```bash
#Show packets with only syn
tcpdunp "tcp[tcpflags] == tcp-syn"

#Show packets with at least a syn(can be also syn-ack)
tcpdump "tcp[tcpflags] & tcp-syn != 0"

#Show packets with at least syn or ack flags
tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) !=0"
```
#### Q: How many packets have only the TCP Reset (RST) flag set?

```bash
tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" | wc -l
#Output
57


```
#### A: `57`


##
#### Q:What is the IP address of the host that sent packets larger than 15000 bytes?
```bash
tcpdump -r traffic.pcap greater 15000 -c 1 -n

#Output
07:18:24.967023 IP 185.117.80.53.80 > 192.168.124.137.60518: Flags [.], seq 2140876081:2140896901, ack 741991605, win 235, options [nop,nop,TS val 2226566282 ecr 3054280184], length 20820: HTTP

```
#### A: `185.117.80.53`

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
#### Q:What is the MAC address of the host that sent an ARP request?
```bash
tcpdump -r traffic.pcap -e -c 1 | grep -i "arp"
#Output


07:18:29.940761 52:54:00:7c:d3:5b (oui Unknown) > Broadcast, ethertype ARP (0x0806), length 42: Request who-has ip-192-168-124-137.ec2.internal tell ip-192-168-124-148.ec2.internal, length 28

```
#### A:`52:54:00:7c:d3:5b`
## You completed the room!!!