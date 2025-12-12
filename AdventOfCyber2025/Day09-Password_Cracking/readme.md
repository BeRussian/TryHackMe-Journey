## Walkthrough of Day* - 


## Theory - What will we learn?
* Crack PDF and ZIP files with password encryption
* dictionary and brute-force attacks methods
* The importance of using strong, complex passwords to defend against these attacks.



### DIctionary attacks
* using predefined list (like rockyou.txt)

### Mask Attaks
* Bruteforce attack --> Try every possible combination until found the currect password
    * The big factor here is the time that grows exponentially 
    * can take years
* Mask Attacks --> Limit guesses to spefific format
    * Aim to reduce time 
    * Example: Try all guesses of 3 lowercase letter followd by 2 digits


### Practical Password cracking Roadmap
1. Start with wordlist like `rockyou.txt`
2. If fails -> Move to targeted wordlist using tools like `cupp`
3. If fails --> Try mask wordlist using tools like `crunch`
* Important notice --> Use GPU accelerated cracking with tools like `hashcat`


## Exercise
Lets connect to the target via ssh
`ssh ubuntu@10.64.159.133`
password
`AOC2025Ubuntu!`

``` bash
ubuntu@tryhackme:~$ cd Desktop/
ubuntu@tryhackme:~/Desktop$ ls
#Output --> flag.pdf  flag.zip  
```
We see 2 files, lets download them using scp
```bash
scp ubuntu@10.64.159.133:/home/ubuntu/Desktop/flag.zip .
scp ubuntu@10.64.159.133:/home/ubuntu/Desktop/flag.pdf .
```
Both files are encrypted with password
lets use john to crack both password

```bash
pdf2john flag.pdf > pdfhash
zip2john flag.zip > ziphash

john --wordlist=/usr/share/wordlist/rockyou.txt pdfhash

john --wordlist=/usr/share/wordlist/rockyou.txt ziphash
```

```bash
#Output
naughtylist      (flag.pdf)     
winter4ever      (flag.zip/flag.txt)     

```
All if left is to open the files and see the flags
### PDF --> `THM{Cr4ck1ng_PDFs_1s_34$y}`
### ZIP --> `THM{Cr4ck1n6_z1p$_1s_34$yyyy}`



### Answer to question 1 ``
* 

##
## Answers

* 
##
#### Q:  

#### A: ``

##
#### Q: 

#### A: ``


##
#### Q: 

#### A: ``

##
#### Q: 

#### A: ``

##
#### Q: 
#### A: ``

## You completed the room!!!