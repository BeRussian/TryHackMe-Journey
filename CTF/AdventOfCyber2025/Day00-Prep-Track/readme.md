## Walkthrough For Prep-Track

### Challenge 1 - Password Pandemonium

we need to create strong password with
1. Enter a password with at least 12 characters.

2. Include uppercase, lowercase, numbers, and symbols.

3. Ensure it isn’t in the breach database.

password --> `HackMeMister420!`

Flag --> `THM{StrongStart}`


### Challenge 2 - The Suspicious Chocolate.exe

we scan the chocolate.exe file using "VirusTotal"
We detect its a trojan malware
Lets flag it as Malicious

Flag --> `THM{NotSoSweet}`

### Challenge 3 — Welcome to the AttackBox!

We get a linux command line shell
Our task is to find the welcome.txt file

```bash
    pwd
    /home/newrecruit
    ls
    challenges/
    cd challenges
    pwd
    /home/newrecruit/challenges
    ls
    welcome.txt
    cat welcome.txt
    Welcome to the AttackBox, recruit. The real training starts now.
    THM{Ready2Hack}
```

Flag --> `THM{Ready2Hack}`

### Challenge 4 — The CMD Conundrum

Same challenge as before only this time
we need to find the hidden_flag.txt file inside

```bash
> dir /a
        readme.txt
 <DIR>  mystery_data
> type readme.txt
System shows signs of tampering. Investigate the mystery_data directory.
> cd mystery_data
> dir 
        notes.txt
> type notes.txt
Some logs were wiped. Hidden artifacts may still remain...
> dir /a
        notes.txt
        hidden_flag.txt  (hidden)
> type hidden_flag.txt
Accessing: hidden_flag.txt
THM{WhereIsMcSkidy}
```

Flag --> `THM{WhereIsMcSkidy}`

### Challenge 5 - Linux Lore
```again find a file in linux machine
cd home
$ 
mcskidy
$ 
/home $ cd mcskidy
$ 
readme.txt
$ 
Delivery drones are glitching. Check hidden files for clues.
$ 
.secret_message  readme.txt
$ 
🐧 Hidden messages, secret files — McSkidy sure knew his way around Linux.
THM{TrustNoBunny}
```

Flag --> `THM{TrustNoBunny}`

### Challenge 6 — The Leak in the List

We use Have I Been Pawned on the mail:
`mcskidy@tbfc.com`


Flag --> `THM{LeakedAndFound}`

### Challenge 7 — WiFi Woes in Wareville
Again we need to create new password
i used the same one as Challenge 1 --> `HackMeMister420!`


Flag --> `THM{NoMoreDefault}`

### Challenge 8 — The App Trap

We need to check the premmisions of every app
And fine the one with unusual permissions

The `Eastmas Scheduler` App has password vaule permission
lets revoke it -->

Flag --> `THM{AppTrapped}`

### Challenge 9 — The Chatbot Confession

We need to read the messages in the chat and find
the messages containing sensitive info
1. https://internal.tbfc.local/admin --> Link
2. Email credentials as requested: user festive.ops and password SnowGlobe#2025. --> Credentials
3. token: sk-live-1a2b3c4d5e6f7g8h --> Hidden token


Flag --> `THM{DontFeedTheBot}`

### Challenge 10 — The Bunny’s Browser Trail
Flag the unusuall web request
```
200 GET /admin/panel • BunnyOS (HopSecBot)
User-Agent: BunnyOS/1.0 (HopSecBot)
```


Flag --> `THM{EastmasIsComing}`

