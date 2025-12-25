## Walkthrough of Day 11 - XSS - Merry XSSMas 



## Theory - What will we learn?
<<<<<<< HEAD
* XSS Vulnerability
* How to exploit?
* How to prevent?
=======
* 
* 
* 
>>>>>>> 6a666f76db8a084b5fac52dd6c4b0dba32014466



### Info
<<<<<<< HEAD
* XSS - Cross Site Scripting
* Inject Malicous code Form or A comment on a WebApp that is visible to other users
* Allows the attack to: 
    * steal credentials
    * deface pages
    * impersonate users  

### Reflected XSS
* Lets look at the link below:

`https://trygiftme.thm/search?term=<script>alert( atob("VEhNe0V2aWxfQnVubnl9") )</script>`
* We see JS script command `atob`, This takes base64 And converts to ascii
* Lets Decode `VEhNe0V2aWxfQnVubnl9` using cyberchef --> 
### Answer to question 2 ``THM{Evil_Bunny}``

### Reflected XSS
* This type of attack includes Uploading malicous script into the web-app
* Then every victim that runs the infected page on the webapp will run the malicous code
* Type of `set-and-forget`

Lets look at the Post Request

```
POST /post/comment HTTP/1.1
Host: tgm.review-your-gifts.thm

postId=3
name=Tony Baritone
email=tony@normal-person-i-swear.net
comment=<script>alert(atob("VEhNe0V2aWxfU3RvcmVkX0VnZ30="))</script> + "This gift set my carpet on fire but my kid loved it!"
```
* Again `atob` function, lets decrypt the base64 string -->
### Answer to question 3 `THM{Evil_Stored_Egg}`

### So how we prevent XSS?
* Sanitize the input!!! Only allow input of strings
* Instead of `innerHTML` propery, use `textContent` to transorm the malicous commands to simple strings
* Make Cookies secure to prevent stealing session cookies


### Exploiting Reflected XSS
* Lets check the site
* We can search comments and upload new one
* Lest exploit reflected XSS by entering in the search box
`<script>alert('Reflected Meow Meow')</script>`
* We again get the flag `Flag: THM{Evil_Bunny}`
* Lest check Stored XSS by injecting code into the upload new comment section
* `<script>alert('Stored Meow Meow')</script>`
* We again get the flag `THM{Evil_Stored_Egg}`
##
## Answers


#### Q:  Which type of XSS attack requires payloads to be persisted on the backend?


#### A: `stored`

##
#### Q: What's the reflected XSS flag?

#### A: `THM{Evil_Bunny}`


##
#### Q: What's the stored XSS flag?

#### A: `THM{Evil_Stored_Egg}`

##

=======
* 




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
>>>>>>> 6a666f76db8a084b5fac52dd6c4b0dba32014466

## You completed the room!!!