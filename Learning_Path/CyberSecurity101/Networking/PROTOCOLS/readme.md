 

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

#### Q: Which SMTP command indicates that the client will start the contents of the email message?



#### A: `DATA`

#### Q: What does the email client send to indicate that the email message has been fully entered?



#### A: `.`

## POP3
* post office protocol 3
* used to allow client to comuunicate with mail server and get email messages

`Common pop3 commands`
```
USER <username> identifies the user
PASS <password> provides the user’s password
STAT requests the number of messages and total size
LIST lists all messages and their sizes
RETR <message_number> retrieves the specified message
DELE <message_number> marks a message for deletion
QUIT ends the POP3 session applying changes, such as deletions
```

#### Q: Looking at the traffic exchange, what is the name of the POP3 server running on the remote server?

`+OK [XCLIENT] Dovecot (Ubuntu) ready.`
#### A: `Dovecot`

#### Q: Use telnet to connect to 10.65.150.139’s POP3 server. What is the flag contained in the fourth message?
* problem may occur when connection from VM, use THM attack box if you see the error 

```
-ERR [AUTH] Plaintext authentication disallowed on non-secure (SSL/TLS) connections.

```
* connect to telnet server with
`telnet IP 110`
```pop3
AUTH 
USER linda
PASS Pa$$123
STAT # TO CHECK CONNECTION SUCCESS
LIST # list all email by number
RETR $ID # Retrive each one of the email until flag is found
##Flag found in mail 4

```
#### A: `THM{TELNET_RETR_EMAIL}`


## IMAP
* what if you want to check your email both from desktop and smartphone?
* IMAP allows synchronization  of messages

```bash

LOGIN <username> <password>
#Choose with mailbox to work with
SELECT <mailbox>
#Read email, need to specify which part of the email
FETCH <mail_number> <data_item_name>
# example: fetch 3 body[]

#Move/copy mail to another mail box
MOVE <sequence_set> <mailbox>
COPY <sequence_set> <data_item_name>

#EXIT
LOGOUT 
```
 


#### Q: What IMAP command retrieves the fourth email message?
* First login
```
telnet IP 143
```
* Enter credentials from preivious task 
```
A LOGIN linda Pa$$123
```
* select the inbox to view the 4th mail
```
B SELECT inbox
```
* Print the body of 4th mail
```
C FETCH 4 body[]
```
#### FLAG --> `THM{TELNET_RETR_EMAIL}`

#### A: `FETCH 4 body[]`

## Summery
Protocol --	Transport Protocol ---	Default Port Number

TELNET  ------- TCP -------	23

DNS -------	UDP or TCP ---	53

HTTP --------- TCP -------	80

HTTPS -------	TCP	------- 443

FTP	------- TCP -------	21

SMTP -------	TCP -------	25

POP3 -------	TCP -------	110

IMAP -------	TCP -------	143
## You completed the room!!!