## Walkthrough of Day 18 | The Egg Shell File 



## Theory - What will we learn?
* Learn about obfuscation, why and where it is used.
* Learn the difference between encoding, encryption, and obfuscation.
* Learn about obfuscation and the common techniques.
* Use CyberChef to recover plaintext safely.

*NOTE*
Its best to connect to the VM using `xfreerdp3`
```
xfreerdp3 /v:10.65.189.40  /u:Administrator /p:@TryObfusc4t3M393!
```



### Learning cipher 
* ROT1 
    * A -> B , X -> Z
    * `carrot coins go brr` -> `dbsspu dpjot hp css`
* ROT13
    * TryHackMe -> GelUnpxZr
    * GuvfVfFrpergZrffntr -> This Is Secret Message
* XOR
    * convert string to bytes
    * generate a secret key
    * use XOR math operation to encrypt
    * TEXT   * KEY = cipher
    * cipher * KEY = TEXT

### How to detect which cipher
* ROT1 - common words look “one letter off”, spaces stay the same. Easy enough to detect.
* ROT13 - Look for three-letter words. Common ones like  the become gur. And and becomes naq. spaces stay the same.
* Base64 - Long strings containing mostly alphanumeric characters (i.e., A-Z, a-z, 0–9), sometimes with + or /, often ending in = or ==.
* XOR - A bit more tricky. Looks like random symbols but stays the same length as the original. If a short secret was reused, you may notice a tiny repeat every few characters.


### Practical

```ps1
# Start here
# Part 1: Deobfuscation
# ==========================
# TODO (Step 1): Deobfuscate the string present in the $C2B64 variable and place the URL in the $C2 variable,
# then run this script to get the flag.

$C2B64 = "aHR0cHM6Ly9jMi5ub3J0aHBvbGUudGhtL2V4Zmls"
 
# ==========================
```
* Copy the string
* We see lower and upper case letters with numbers
* lets try base64
* `https://c2.northpole.thm/exfil`
Lest modify the script and run
```ps1
$C2    = "https://c2.northpole.thm/exfil"  
```
### Flag #1 ---> `THM{C2_De0bfuscation_29838}`

```ps1
# Part 2: Obfuscation
# ==========================
# TODO (Step 2): Obfuscate the API key using XOR single-byte key 0x37 and convert to hexidecimal,
# then add the hex string to the $ObfAPieEy variable.
# Then run this script again to receive Flag #2 from the validator.
$ApiKey = "CANDY-CANE-API-KEY"
# ========================== 
```
* copy the string `CANDY-CANE-API-KEY`
* First step: encode using xor with the key `0x37`
* Second step: Convert output to hex
* Insert the output to the script --->
```ps1
$ObfAPIKEY = Invoke-XorDecode -Hex "74 76 79 73 6e 1a 74 76 79 72 1a 76 67 7e 1a 7c 72 6e" -Key 0x37
```
* run the script to get the second and final flag
### ### Flag #2 ---> `THM{API_Obfusc4tion_ftw_0283}`


##
## You completed the room!!!