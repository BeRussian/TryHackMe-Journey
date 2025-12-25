## Walkthrough of Day Day 13 - YARA Rules - YARA mean one!



## Theory - What will we learn?
* Understand the basic concept of YARA.
* Learn when and why we need to use YARA rules.
* Explore different types of YARA rules.
* Learn how to write YARA rules.
* Practically detect malicious indicators using YARA.

### What is yara?
* A tool used to find malware by searching patterns inside files
* YARA scans code, files, and memory traces that reveal Malware.

### When to use Yara?
* Post-incident analysis
    * Find traces of malware after an attack
* Threat Hunting
    * Look for known malwares families
* Intelligence-based scans
    * Use existing rules to detect -->
    * `IOC(indicator of compromise)`
* Memory analysis
    * Examine active process in memory dump to find malicious code
### Why use YARA?
* Speed
    * Dont need to wait for the Anti-Virus to update
    * Quicly scan large sets of files
* Flexibility
    * Can detect, Strings, Vinary patterns and complex logic
* Control
    * Every orgaization can classify what is malicous
* Shareability
    * Everyone can download existing yara rules and apply easialy
* Visibility
    * Helps orgenize the info about the attack

### How to build Yara rule
* Metadata -> Info about the rule
* Strings -> defind veriables to look for
* Conditions -> Define when rules triggers

`Example`
```yara
rule TBFC_KingMalhare_Trace
{
    meta:
        author = "Defender of SOC-mas"
        description = "Detects traces of King Malhare’s malware"
        date = "2025-10-10"
    strings:
        $s1 = "rundll32.exe" fullword ascii
        $s2 = "msvcrt.dll" fullword wide
        $url1 = /http:\/\/.*malhare.*/ nocase
    condition:
        any of them
}
```

### Types of strings
* Text strings
    * `$TBFC_string = "Christmas"`
    * `nocase` --> in case sensitive search
    * `wide` ascii --> Search both ASCII&UTF-16(exe)
    * `xor` --> check for encoded variations using xor
    * `base64` -> Check for encoded payload via base64
* Hexadecimal strings
    ```
    strings:
    $mz = { 4D 5A 90 00 }   // MZ header of a Windows executable
    $hex_string = { E3 41 ?? C8 G? VB }
    ```
* Regular Expressions
```
strings:
    $url = /http:\/\/.*malhare.*/ nocase
    $cmd = /powershell.*-enc\s+[A-Za-z0-9+/=]+/ nocase
```

### Types of Conditions
* Match a single string
    * $xman
* Match any
    * any of them
* Match all strings
    * all of them
* Combined use
    * ($s1 or $s2) and not $benign
* Existing conditions
    * (filesize > 700KB) and  (filesize < 2MB)
    * hash.md5(0, filesize) == "5bf1fd927f3676918f55c3cd25132d78"
    * entrypoint(After the header) --> uint8(entrypoint) == 0x60

### Practice
* yare rules must be saved in .yar file
* running scan syntax
`yara -r icedid_starter.yar C:\`
* Yara flags
    * -r --> recursive scan
    * -s --> Prints the strings match







##
## Answers

#### Q:  How many images contain the string TBFC?
* Lets create a yara rule to find the strings "TBFC"
```
rule TBFC1
{
    meta:
        author = "BeRussian710"
        description = "Detects TBFC: "
        date = "2025-12-18"
    strings:
        $s1 = "TBFC"
    condition:
        $s1
}

```
* run with 
`yara TBFC1.yar /home/ubuntu/Downloads/easter`

```bash
#Output
TBFC1 /home/ubuntu/Downloads/easter/easter46.jpg
TBFC1 /home/ubuntu/Downloads/easter/easter16.jpg
TBFC1 /home/ubuntu/Downloads/easter/easter10.jpg
TBFC1 /home/ubuntu/Downloads/easter/easter52.jpg
TBFC1 /home/ubuntu/Downloads/easter/easter25.jpg

```


#### A: `5`

##
#### Q: What regex would you use to match a string that begins with TBFC: followed by one or more alphanumeric ASCII characters?



#### A: `/TBFC:[A-Za-z0-9]+/`


##
#### Q: What is the message sent by McSkidy?


* Lets modify the rule
```
rule TBFC1
{
    meta:
        author = "BeRussian710"
        description = "Detects TBFC: "
        date = "2025-12-18"
    strings:
        $s1 = "TBFC"
        $s2 = /TBFC:[A-Za-z0-9]+/
    condition:
        $2
}
```
* run with `yara -s TBFC1.yar . `

```bash
#Output
TBFC1 ./easter/easter46.jpg
0x2f78a:$s1: TBFC:HopSec
TBFC1 ./easter/easter16.jpg
0x3bb7f7:$s1: TBFC:me
TBFC1 ./easter/easter10.jpg
0x137da8:$s1: TBFC:Find
TBFC1 ./easter/easter52.jpg
0x2a2ad2:$s1: TBFC:Island
TBFC1 ./easter/easter25.jpg
0x42c778:$s1: TBFC:in

```
#### A: `Find me in HopSec Island`


## You completed the room!!!