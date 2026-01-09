 

## Walkthrough of Networking Core Protocols Room






## Theory - What will we learn?
* DNS & WHOIS
* HTTP/S
* FTP
* SMTP
* POP3
* IMAP



### DNS
* Domain name system
* port 53 `UDP`
* Responsible for converting ip to domain
* Example 8.8.8.8 converts to google.com
* Operates on Application layer(7)

`DNS records`
* A Record
    * ipv4 
    * example.com.     IN     A       93.184.216.34
* AAAA Record
    * IPV6 Adresses
    * example.com.     IN     AAAA    2606:2800:21f:cb07:6820:80da:af6b:8b2c
* CNMAE Record
    * CNAME stands for Canonical Name
    * Holds other domain that the main domain redirecs to
    * www.example.com.     IN     CNAME     example.com.

* MX Record
    * Hold the data for the Mail server(Mail Exchange) for the domain
    * example.com.     IN     MX     10 mail.example.com.

`NOTE`
* to quickly check domain ip you can use

`nslookup $DOMAIN`

#### Q: 

#### A: `AAAA`

#### Q: Which DNS record type refers to the email server?

#### A: `MX`

* More over if you want to get info about the Owner of a spesific domain you can simply do it with 

`whois $DOMAIN`
#### Q: When was the x.com record created? Provide the answer in YYYY-MM-DD format.
```bash                                             whois x.com    
   Domain Name: X.COM
   Updated Date: 2024-12-03T21:03:37Z
   Creation Date: 1993-04-02T05:00:00Z
```
#### A: `1993-04-02`

#### Q: When was the twitter.com record created? Provide the answer in YYYY-MM-DD format.

```bash                                             whois twitter.com | grep Creation
connect: Network is unreachable
   Creation Date: 2000-01-21T16:28:17Z

```
#### A: `2000-01-21`

## HTTP(S)
http  -> 80
https -> 443
4 types of HTTP Request:
1. GET --> get specific webpage
2. POST   -> allows us to send data to the webserver
3. PUT    -> create/update resource on the web-server
* Change user's ID
4. DELETE -> Delete resource on web-server

`NOTE`
if you send 100 PUT/DELETE request, they will only take affect ones, thats why you need them and not just use POST
#### Q: 

`telnet 10.64.151.109 80`
* After connection is established -->

`GET flag.html`

`<div class="hidden-text">THM{TELNET-HTTP}</div>
`
* What we did? we used telnet tool to connect to port 80 via tcp and send a get request
#### TIP -->  We can also use curl

`curl http://10.64.151.109/flag.html
`
#### A: `THM{TELNET-HTTP}`

## FTP
* port 21
* has anonymous mode
* `get $file` -> download a file
* `put $local_file`  -> Upload a file
## SMTP
* simple mail transfer protocol
* most common mail protocol
* Lets send a mail using telnet

```bash
telnet $IP 25
#START SMTP SESSION
HELO

MAIL FROM: <$SENDER_MAIL>
RCPT TO: <$TO_MAIL>


#Start Actual message
DATA
# To end data and send mail enter .
.
```
#### Q:Which SMTP command indicates that the client will start the contents of the email message? 

#### A: `DATA`

#### Q:What does the email client send to indicate that the email message has been fully entered? 

#### A: `.`

## POP3


#### Q: 

#### A: ``
## You completed the room!!!