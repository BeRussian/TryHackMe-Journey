## Walktrhoguh for Advent of Cyber day 03 - Splunk Basics - Did you SIEM?


In this room we will analyize log using the SIEM splunk

##
### Lets start with the Investigation
##
`sourcetype=*`

we see 2 sources: `web_traffic` & `firewall_logs`

We are told the local IP of the web server is: `10.10.1.15`

Lets sort all the logs of web_traffic per day
and check which days where unusuall number of requests

`index=main sourcetype=web_traffic | timechart span=1d count`

* `timechart span=1d` --> will divide all requests into 1 day and count them per day  

`index=main sourcetype=web_traffic | timechart span=1d count | sort by count | reverse`

* Print the day with the highest  number of request first
### Answer to question *2*
##
## Proper investigation

Lets check 
1. User agent - Check for unsusuall ones
2. Client IP - Client that tried to connect to the web server
3. path

### User agent
```
Wget/1.21.4	1,240	
zgrab/0.x	1,238	
curl/7.88.1	1,220	
Go-http-client/1.1	1,201	
Havij/1.17 (Automated SQL Injection)	
sqlmap/1.7.9#stable (http://sqlmap.org)	
python-requests/2.28.1
```

### Client ip
 * `198.51.100.55` tried to connect over 45% of the entire network traffic

### Path
```
/search?q=test	666	3.878%	
/item.php?id=1 AND SLEEP(5)--	660	3.843%	
/download?file=../../etc/passwd
```
* We see the attacker tried to inject command into our web server using sql injection
* More over H tried to access /etc/passwd --> WHICH CONTAINS LIST OF ALL USERS IN THE SYSTEM


### Filtering out GOOD Traffic
* Lets filter all good user agents ->
```
index=main sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox*
```

* We are left with only 1 ip that is responsible for the entire communication 
--> `198.51.100.55`
### Answer to question *1*

Command to narrow down ip client that send request from common desktop or mobile browsers:
```
sourcetype=web_traffic user_agent!=*Mozilla* user_agent!=*Chrome* user_agent!=*Safari* user_agent!=*Firefox* | stats count by client_ip | sort -count | head 5
```

### Understanding the attack -> Tracing the Attack Chain

Lets follow the attacker ip, What did he do on the system?
`sourcetype=web_traffic client_ip="198.51.100.55" AND path IN ("/.env", "/*phpinfo*", "/.git*") | table _time, path, user_agent, status`

* We can see from the results the attacker tried to access sensitive info on the web-server but encouterd a 401/403/404 response code -->Fail
* We also see the attacker used tools lige `curl` and `wget` 

```
sourcetype=web_traffic client_ip="*" AND path="*..\/..\/*" OR path="*redirect*" | stats count by path
```

``` 
#Output
/?redirect=http://evil.site	633
/download?file=../../etc/passwd	658
```
### Answer to question *3* --> `658`

#### We see the attacker tried to access sensitive files and check for sql injection vulnerabilities


### Lets check which sql-injection tool the attacker used -->
```
sourcetype=web_traffic client_ip="*" AND user_agent IN ("*sqlmap*", "*Havij*") AND path != "/item.php?id=1"| table _time, path, status
```

We can see many command injection
#### status Code 504 usually confirms a successful sql-injection on the command SLEEP(5)


### Lest check what files the attacker tried to download -->
````
sourcetype=web_traffic client_ip="*" AND path IN ("*backup.zip*", "*logs.tar.gz*") | table _time path, user_agent
````
### Output
````
/logs.tar.gz	Go-http-client/1.1	93
/logs.tar.gz	Wget/1.21.4	86
/logs.tar.gz	curl/7.88.1	85
/logs.tar.gz	zgrab/0.x
````
* We can see the attacker tried to download the logs.tar.gz file using diffrent tools like `wget` \ `curl` and `zgrab`

### Lets check if the user succedded  remote code executation on the web server -->
```
sourcetype=web_traffic client_ip="*" AND path IN ("*bunnylock.bin*", "*shell.php?cmd=*") | table _time, path, user_agent, status
```

Output:
```
	/shell.php?cmd=whoami	Ruby/2.7.0 (Webshell Runner)	500
	/shell.php?cmd=chmod%20+x%20bunnylock.bin	python-requests/2.28.1	500
	/shell.php?cmd=./bunnylock.bin	Ruby/2.7.0 (Webshell Runner)	200
```
1. Attacker executed `whoami` command
2. Uploaded a script named `bunnylock.bin`
3. Executed it

### This is bad!

##
## Firewall log Analysis
* after done with the web server logs, lets switch to the `firewall_logs`
```
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | table  action, protocol, src_ip, dest_ip, dest_port, reason
```

Output

```
action	protocol	src_ip	dest_ip	dest_port	reason
ALLOWED	TCP	10.10.1.5	198.51.100.55	8080	C2_CONTACT
ALLOWED	TCP	10.10.1.5	198.51.100.55	8080	C2_CONTACT
ALLOWED	TCP	10.10.1.5	198.51.100.55	8080	C2_CONTACT
```
### Explanation
*  Compromised Server IP (10.10.1.5)
*  Attacker IP (198.51.100.55)
*  Action (Allowed) --> All the network traffic the passed the firewall
* reason C2_contact -> connection to Command & Controll server of the attacker 

### Question: how much data did the attacker copied and transfferd to the C2 server?

```
sourcetype=firewall_logs src_ip="10.10.1.5" AND dest_ip="<REDACTED>" AND action="ALLOWED" | stats sum(bytes_transferred) by src_ip
```

Output

```
src_ip	sum(bytes_transferred)
10.10.1.5	126167
```
### Answer to question *5* --> `126167`

### Explanation
* Attacker trannsfered `126167` bytes
* Which is 123.3 kb

## Answers

#### Q1: What is the attacker IP found attacking and compromising the web server?

#### Answer: `198.51.100.55`

`Explanation: Check the ip that send the most traffic from the unsusuual user agets`

##
#### Q2: Which day was the peak traffic in the logs? (Format: YYYY-MM-DD)

#### Answer: `2025-10-12`

#### Q3: What is the count of Havij user_agent events found in the logs?

#### Answer: `993`


#### Q4: How many path traversal attempts to access sensitive files on the server were observed?
#### Answer: `658`


#### Q5: Examine the firewall logs. How many bytes were transferred to the C2 server IP from the compromised web server?

#### Answer: `126167`




