## Walkthrough of Day Day 12 - Phishmas Greetings 


## Theory - What will we learn?
* Spotting phishing emails
* Learn trending phishing techniques
* Understand the differences between spam and phishing



### Info
Porpuse of Phishing Emails:
* Credential theft: Tricking users into revealing passwords or login details.
* Malware delivery: Disguising malicious attachments or links as safe content.
* Data exfiltration: Gathering sensitive company or personal information.
* Financial fraud: Persuading victims to transfer money or approve fake invoices.

### Key diffrences between Phishing and Spam
* Spam focuses on quantity over precision
* 4 Main Intenrations of spam mail:
    * Ads
    * Scams(get rich quickly)
    * Traffic generation(clickbait)
    * Data harvesting -> Collect active email addresses

* #### How to differ? 
* #### Look for intentions behind the mail 

### Phishing techniques 
1. Impersonation --> Check if the From(Sender) is a company mail or a free mail(like gmail)
    * Example(Impersonat to the ceo or ciso of the company)
2. Social Engeneering - 
    * Impersonation - 
    * Sense of urgency - Please act immediatly or credit card gets blocked
    * Side channel -> Im currently unreachable by phone, please reach me by another mail...
    * Malicious intention - Send me password / VPN credentials
3. Typosquatting and Punycode - (go0gle isntead of google/ тrуhackme.com)
    * Tip to Uncover --> Cheack `return-path` in the email header
4. Spoffing -> Email looks real  but Authentication fails
    * Tip > Check Authentication-results In the email headers
    *  if SPF, DKIM, and DMARC(security checks) failed, mail is fake  
    * SPF: Says which servers are allowed to send emails for a domain (like a list of approved senders).
    * DKIM: Adds a digital signature to prove the message wasn’t changed and really came from that domain.
    * DMARC: Uses SPF and DKIM to decide what to do if something looks fake (for example, send it to spam or block it).
    * More over check `return-path` to see actual mail
5. Malicious Attachments
    * Usually comes with additional social engineering  text
    * HTA/HTML files are commonly used for phishing
    *  Once opened, these files can install malware, steal passwords, or give attackers access to the device or network
6. Side Channel Communications
    * When attacker asks victim to move to another channel lije sms/whatsapp/telegram/phone call / shared document platform

##

#### Q: Classify the 1st email, what's the flag?
* Phishing
* Senso of Urgency = " Call PayPal immediately"
* Fake Invoice
* Spoofing = "Return-Path	bounces`+SRS=qVbic=PZ@bbunny378.onmicrosoft.com"`
* spf=fail dkim=fail dmarc=fail 
#### A: `THM{yougotnumber1-keep-it-going}`

#### Q: Classify the 2nd email. What's the flag?
* Phishing
* Impersonation --> "McSkidy"
* Malicious Attachment --> mp3 is actually html
* Spoofing --> return address is `zxwsedr@easterbb.com`
#### A: `THM{nmumber2-was-not-tha-thard!}`

#### Q: Classify the  3rd email, what's the flag?
* Phishing
* Impersonation --> "McSkidy"
* Senso of Urgency = "This is urgent please action immediately."
* Social Engineering Text --> "Please create a new VPN access for me"
#### A: `THM{Impersonation-is-areal-thing-keepIt}`

#### Q: Classify the 4th email, what's the flag?
* Impersonation --> "TBFC HR Department"
* External Sender Domain -> "Using DropBox"
* Social Engineering Text --> "Annual Salary Raise Approval"
#### A: `THM{Get-back-SOC-mas!!}`

#### Q: Classify the 5th email, what's the flag?
* Spam
#### A: `THM{It-was-just-a-sp4m!!}`

#### Q: Classify the 6th email, what's the flag?
* Typosquatting/Punycodes --> tb`ƒ`c.com
* Impersonation -> TBFC-IT
* Social Engineering Text -> "Christmas
  Laptop Upgrade Agreement"
#### A: `THM{number6-is-the-last-one!-DX!`




## You completed the room!!!