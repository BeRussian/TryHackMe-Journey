## Walkthrough of Day 17 - CyberChef - Hoperation Save McSkidy 



## Theory - What will we learn?
* Introduction to encoding/decoding
* Learn how to use CyberChef
* Identify useful information in web applications through HTTP headers



### Encoding Vs Encryption
* Encoding -> used to convert info between diffrent systems.
    * Fast
    * Example: base64
* Encryption
    * Used to make data unreadble by using a speacial key knowing only to the sender and the reciver
    * Slow
    * Example: TLS

### First Lock - Outer Gate
* Guards name is `CottonTail`
* `Q290dG9uVGFpbA==`
* Magic Question is `What is the password for this level?`
* `V2hhdCBpcyB0aGUgcGFzc3dvcmQgZm9yIHRoaXMgbGV2ZWw/`
* Use the chat to ask the gaurd the question in base64
* Answer: SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IFNXRnRjMjltYkhWbVpuaz0=
* Decoded answer: Here is the password: SWFtc29mbHVmZnk=
* Decoded Password: `Iamsofluffy`

So final credentials for Lock #1
is 
Username `Q290dG9uVGFpbA==`
Password `Iamsofluffy`
🏴 Guard House lock has been breached! Proceeding to Inner Castle in 2s… 
### Second Lock - Outer Wall
* Guards name `CarrotHelm` 
* Encoded b64 gaurds name `Q2Fycm90SGVsbQ==` 
* Magic question is `Did you change the password?`
* Convert to b64 --> `RGlkIHlvdSBjaGFuZ2UgdGhlIHBhc3N3b3JkPw==`
* Ask in chat --> `SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IFUxaFNkbUpIVWpWaU0xWXdZakpPYjFsWE5XNWFWMnd3U1ZFOVBRPT0=` 
* Decode answer `Here is the password: U1hSdmJHUjViM1YwYjJOb1lXNW5aV2wwSVE9PQ==`
* Decode password `SXRvbGR5b3V0b2NoYW5nZWl0IQ==`
* Decode password again `Itoldyoutochangeit!`

Final credentials
* USERNAME = `Q2Fycm90SGVsbQ==`
* PASSWORD = `Itoldyoutochangeit!`
🏴 Guard House lock has been breached! Proceeding to Inner Castle in 2s… 
### Third Lock - Guard House

* Guards name `LongEars` 
* Encoded b64 gaurds name `TG9uZ0VhcnM=` 
* Question to ask the guard `Password please.`
* Convert to b64 --> `UGFzc3dvcmQgcGxlYXNlLg==`
* Ask in chat --> `SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IFUxaFNkbUpIVWpWaU0xWXdZakpPYjFsWE5XNWFWMnd3U1ZFOVBRPT0=` 
* Decode answer `SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IElRd0ZGakFXQmdzZg==`
* Decode password `Here is the password: IQwFFjAWBgsf`
* XOR key `cyberchef`
* Recipe `From base64` -> `XOR (key: cyberchef)`

Final credentials
* USERNAME = `TG9uZ0VhcnM=`
* PASSWORD = `BugsBunny`
🏴 Guard House lock has been breached! Proceeding to Inner Castle in 2s… 

### Fourth Lock - Inner Castle
* Guards name `Lenny` 
* Encoded b64 gaurds name `TGVubnk=` 
* Question to ask the guard `Password please.`
* Convert to b64 --> `UGFzc3dvcmQgcGxlYXNlLg==`
* Ask in chat --> `SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IGI0YzBiZTdkN2U5N2FiNzRjMTMwOTFiNzY4MjVjZjM5` 
* Decode answer `Here is the password: b4c0be7d7e97ab74c13091b76825cf39`
* We can see from the DeBugger the password is encoded in md5 hash
* lets use https://crackstation.net/ to decode
* Decoded password is  `passw0rd1`

Final credentials
* USERNAME = `TGVubnk=`
* PASSWORD = `passw0rd1`
🏴 Guard House lock has been breached! Proceeding to Inner Castle in 2s… 

### Fifth Lock - Prison Tower
* Guards name `Carl` 
* Encoded b64 gaurds name `Q2FybA==` 
* Question to ask the guard `Password please.`
* Convert to b64 --> `UGFzc3dvcmQgcGxlYXNlLg==`
* Ask in chat --> `SGVyZSBpcyB0aGUgcGFzc3dvcmQ6IGI0YzBiZTdkN2U5N2FiNzRjMTMwOTFiNzY4MjVjZjM5` 
* Decode answer `Here is the password: IxtDWjODKNLBVEIFOuyDTt==`
* Lets check which algorithem we got--->
* Encryption = `R3`
* XOR key `cyberchef`
* 
```
case "R3":
            // CyberChef: ROT13 => From Base64 => XOR(key=recipeKey)
            const exed = bytesToBase64(xorWithKey(toBytes(tp), toBytes(recipeKey || "hare")));
            tp = rot13(exed);
```
* Cyberchef recipe --> 
* `ROT13 => From Base64 => XOR(key=cyberchef)`

Final credentials
* USERNAME = `Q2FybA==`
* PASSWORD = `51rBr34chBl0ck3r`
🏴 Guard House lock has been breached! Proceeding to Inner Castle in 2s… 
##
#### Final flag
#### THM{M3D13V4L_D3C0D3R_4D3P7}

##


## You completed the room!!!