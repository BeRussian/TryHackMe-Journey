## Cheet-Sheet for john
`sudo apt-get install john`

## Basic formats

```bash
# Specify format to crack(raw-md5,nt,)
--format=

# List all john avalible formats
john --list=formats
    --format=raw-md5
    --format=raw-sha1
    --format=raw-sha256
    --format=raw-sha512
    --format=whirlpool


# Cracking /etc/shadow
#You can user hash-id.py to identify the has
wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py

```

## Windows hash's
```bash
# Crack windows password encoded in NThash 
# (previous version of hashing format called NTLM)
    --format=nt

```
## Linux Hash's
```bash
# /etc/shadow contains password hash's
# /etc/passwd contains the type of hash for every user

# 1. user both files to unshadow the hash and save to file
unshadow $PASSWD_FILE $SHADOW_FILE > unshadow.txt

# 2.crack using john
john --wordlist=$WORDLIST --format=sha512crypt unshadowed.txt
# * Usually dont need to specify format, but it workes ether way 
```

## Creating wordlists using JOHN
```bash
#Give john a username to generate possible pass list
john --single --format=raw-sha256 hashes.txt
#Make sure the hash is written in this format inside the file
$USERNAME:$HASH

```
## Cracking Zip & RAR
* If a zip/rar file is encrypted with password, we can brute force it
```bash
zip2john $zip/rar_file > hash.txt
john --wordlist=$LIST hash.txt

#After cracking can extract with
7z x $FILE
unzip $FILE
unrar x $FILE
```
## Cracking SSH keys
* Most times we connect to ssh via user&pass
* There is another way to connect using ssh private key
* this private key is saved in `id_rsa` file
* To authenticate using the private key we need the brute-force the password of the id_rsa file
* lets use `ssh2john`, also knows as `ssh2john.py`
```bash
ssh2john id_rsa > sshhash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt sshhash.txt

```
## Creating Custom Rules
* Like --single mode we can create our own rules to genereate valid passlist
* we can add rules to `/etc/john/john.conf`

* Every rule starts with Az/A0/c
```
Az - take the word and append the regex
A0 - take the work and put the regeq before
c  - Make the first letter Uppercase

[0-9]: Will include numbers 0-9
[0]  : Will include only the number 0
[a]  : Will include only a
[A-z]: Will include both upper and lowercase
[A-Z]: Will include only uppercase letters
[a-z]: Will include only lowercase letters
[!£$%@]: Will include the symbols !, £, $, %, @
```
* For example:
```
[List.Rules:PoloPassword]
cAz"[0-9] [!£$%@]"
```
* c Capitalises first letter
* Az append the rest of the regex after the word
* [0-9] will add 1 digit
* [!£$%@] will add one symbol

TO USE THIS RULE
```bash
john --wordlist=$LIST --rule=$RULE_NAME $FILE_2_CRACK
```
