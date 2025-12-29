## Walkthrough of Day 15 - Web Attack Forensics - Drone Alone



## Theory - What will we learn?
* Detect and analyze malicious web activity through Apache access and error logs
* Investigate OS-level attacker actions using Sysmon data
* Identify and decode suspicious or obfuscated attacker payloads
* Reconstruct the full attack chain using Splunk for Blue Team investigation

### Splunk Analysis
* Lets check for malicous web-server commands
* we want to check the web server logs for malicous requests
* We are looking for:
    * cmd.exe
    * powershell.exe
    * Invoke-Expression
* Lets check the `windows_apache_access` log -> 
* it logs all the web requests to the web-server 
```
index=windows_apache_access (cmd.exe OR powershell OR "powershell.exe" OR "Invoke-Expression") | table _time host clientip uri_path uri_query status
````

* We see 4 events, but the request is encoded using base64

![alt text](image.png)
lets decode this using cyberchef
![alt text](image-1.png)
`T.h.i.s. .i.s. .n.o.w. .M.i.n.e.!. .M.U.A.H.A.A.H.A.A.` --> NOT GOOD
### Answer to question 2 `powershell.exe`
### Check Server side errors
 * Lets look at diffrent log
 * `windows_apache_error` --> logs all the error of the web application
 * Lets check for errors containing:(cmd.exe,powershell , Internal Swever Error)
 ```
 index=windows_apache_error ("cmd.exe" OR "powershell" OR "Internal Server Error")

```
* We see the request we found previously run at the server
* This means the attacker managed to run commands on the webserver 
* and an error as ocorued, `key sign of exploitation attempts`

### Proof Of Compromize
* Lets look at sysmon events(Logs all the Programs that run on the server)
* We want to only look at the logs of the webserver(our case apache),Which its process is called `httpd.exe`
```
index=windows_sysmon ParentImage="*httpd.exe"
```
* Apache process should span worker threads(such as httpd.exe/ php-cgi.exe/python.exe etc....)
* If we see process like cmd.exe or powershell.exe is a proof the attacker as succeseded a seccessful command injection

### Confirm
```
index=windows_sysmon *cmd.exe* *whoami*

```
### Answer to question 1 `whoami.exe`
* This query check what command the `cmd.exe` run
* we see the attacker run an `whoami` command



##
## Answers

#### Q:  What is the reconnaissance executable file name?



#### A: `whoami.exe`

##
#### Q: What executable did the attacker attempt to run through the command injection?



#### A: `PowerShell.exe`



## You completed the room!!!