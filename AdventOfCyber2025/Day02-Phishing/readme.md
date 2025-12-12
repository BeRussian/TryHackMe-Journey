## Walkthrough for Advent of Cyber 2025 - Day 2


## Learning:
Human hacking -> focuses on making the victim:
1. share a password
2. open a malicious file
3. aprove a payment

most social engenniring attack relay on psychological factors like:
1. urgency
2. curiosity
3. authority

## Phishing:
the most common phishing technic is via email
but nowdays we have also:
1. smishing - short text messages
2. vishing - voice calls
3. quishing - QR codes
4. social-media direct messages

How to uncover phishing email? S.T.O.P *2

S - Suspicious?
T - Telling me to click something?
O - Offering me an amazing deal?
P - Pushing me to do something now?


S - Slow down. Scammers run on your adrenaline.
T - Type the address yourself. Don’t use the message’s link.
O - Open nothing unexpected. Verify first.
P - Prove the sender. Check the real From address/number, not just the display name.


Practical
LETS DO A PHISHING ATTACK
Well use setoolkit for this one
Just follow the steps below
```
 1) Social-Engineering Attacks
    5) Mass Mailer Attack
        1) E-Mail Attack Single Email Address

Send email to: factory@wareville.thm
Use your own server or open relay
From Address: updates@flyingdeer.thm
From name: Flying Deer
username : *LEAVE BLANK*
PASSWORD : *LEAVE BLANK*
SMTP SERVER : 10.80.157.65
SMTP PORT : 25

Flag this message as high priority: NO
Do you want to attach a file: n
Do you want to attach an inline file: n

Email subject: Shipping Schedule Changes
Message Body: Must have the line below:
http://MACHING_IP_HOSTING_THE_FAKE_WEBSITE:8000
END

```
now wait until you see the line below
```
[2025-12-05 08:33:13] Captured -> username: admin    password: unranked-wisdom-anthem    from: 10.80.157.65
```
Credentials:
    Username: admin
    Password: unranked-wisdom-anthem

Lest browse to http://10.80.157.65 and use our Password and the `factory` user

Success
Lets read the mail With the title 
` Urgent: Production & Shipping Request — 1984000 Units (Next 2 Weeks) `
### Answer --> 1984000 








