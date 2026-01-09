## Cheatsheet for Gobuster tool

### Usfull flags
```bash
#Specify URL/IP
-u $URL

# Specify wordlist
-w $PATH

# Control number of active threads
-t $NUMBER

# Set amount of tine between requests
--delay $SECONDS

#Output results to a file
-o $FILE

#troubleshoot errors
```

### dir
* allows finding hidden directories on a web-application

```bash
# Pass a cookie(to achive authentication)
-c $COOKIE

# Check for spesicific extensions
-x $[.php/.txt/.js]

#Specify entire header to send in the request
-H $request_header

#Skip checking web-certificate
-k

#Dont output failed attempts
-n

#Specify username and password 
-U $username
-p $PASSWORD

#Specify which status code in the response to display
-s $CODE
#Which status code dont display
-b $CODE

#Follow redirections of the website
-r

```
#### Examples
```bash
#Basic dir brute-force
gobuster dir -u $URL$ -w $WORDLIST

#Check for .php and .js files and increse number of threads and allow redirections
gobuster dir -u "http://www.example.thm" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.js -t 64 -r 
```
#### Usfull wordlists
```
/usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

### dns
* Allows burte-force subdomain
* Example if main domain is `tryhakme.thm`, Possible subdomain is `mobile.tryhackme.thm`

#### Flags
```bash
#specify main domain to enum
-d
#Show CNAME records
-c 
#Show ip address
-i
#
```
#### Example
```bash
gobuster dns -d $Domain -w $wordlist 

```
#### Usfull wordlists
```
/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```
### vhosts
* Virtual hosts allows to host multiple website on the same machine/ip

#### Flags
```bash
#url
-u $URL

#Append the main domain to each request
--append-domain

#Specify domain to append
--domain $DOMAIN
#Specify which HTTP method to use(GET/POST)
--method $METHOD

# Filter out responses with specific length
--exclude-length $NUMBER

#Allow redirections
--follow-redirect


```

#### Examples
```bash
gobuster vhost -u $URL -w $path
gobuster vhost -u "http://10.66.186.36" --domain example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320
```
#### wordlists
```
/usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```