## Walkthrough of Day05 - IDOR - Santa’s Little IDOR


## Theory
What is IDOR attack?
### IDOR --> Insecure Direct Object Reference
### Answer for question 1
Lets look at the link below:

`https://awesome.website.thm/TrackPackage?packageID=1001`

#### Question: What will happen if we change the packageID parameter?
Will we recive info about diffrent package?Not our package?
This can be case of `IDOR`

What is IDOR?
* type of access control vulnerability
* If a web-server dorsnt perform check to ensure the user allowed to access specific data, it can lead to `sensitive info leak`

### Authentication: 
 * The proccess the web-server check who you are(User supllies Username & Password)
  

### Authorization

 * The process of the website check the permissions of the user connectet

 * Example: Does the current user allowd to access the admin page?
 * Does the user allowed to see the package of another user?

 
 `Important notice -> Authorization can happen only after Authentication has completed`


 ### Vertical privilege escalation: 
 * Go up -> Gain more privileges then before
  

### Horizontal privilege escalation

 * Move left or right -> Go to diffrent user on the same level, Gain diffrent permiission then the old user


 `IDOR is usually a form of horizontal privilege escalation`
 ### Answer for question 2 --> `horizontal`
##
## Practical IDOR

* IP `http://10.65.191.229`
* USERNAME `niels`
* PASSWORD `TryHackMe#2025`


Lets test the website for IDOR vulnerability
1. Right click -> Inspect -> Network
* look at the line:
`view_accountinfo?user_id=10`
* If we look at the response on the right we will see
```
{"user_id":10,"username":"niels","email":"niels@webmail.thm","firstname":"Niels","lastname":"Tester","id_number":"NIELS-001","address1":"42 chill Street","address2":"Apt 1","city":"TryTown","state":"THM","postal_code":"42424","country":"Netherlands",

```
#### We see the our user (niels) is user id 10

We can also see another users in the response
```
"child_id":2,"id_number":"8902035555","first_name":"Bilbo","last_name":"Baggins",


{"child_id":3,"id_number":"152312","first_name":"johny","last_name":"doe","

{"child_id":4,"id_number":"JOHNYDOE-554","first_name":"johny","last_name":"doe","

{"child_id":9,"id_number":"TERSTTESTER-605","first_name":"Terst","last_name":"Tester",

{"child_id":10,"id_number":"TEST2TESTER-014","first_name":"Test2","last_name":"Tester"
```
#### Lest try to change the user ID to test IDOR
1. Inspect -> Storage -> Local storage
2. In the `auth_user` change the line below
* {"user_id":10,"email":"niels","role":"parent","name":"niels"}
3. change the user ID value, try 11
4. refresh the page
5. YEY! We get another user

#### This is the basic form of IDOR
#### But what it there is obsfucation of the data?
Lets return to the original user page
1. Next to the bilbo child of the original user there is an eye icon -> `Click it`
2. Inspect the network like we have done previously
3. we see `Mg==` request, this is just 2 in base64
4. lets change this to 3 --> `Mw==`
5. if you look at the response you will see response for child 3

#### Lets look at yet another form of IDOR
#### Only this time the data is in md5 form

1. inspect the network while clicking the edit button next to a childs name, 
2. look at the request
`md5/c81e728d9d4c2f636f067f89cc14862c`
3. using site like crack station lets crack this hash
-->
Cracked (2)
4. Lets try to change it
```bash
echo -n "3" | md5sum
eccbc87e4b5ce2fe28308fd9f2a7baf3  -
```
5. Edit and resend-->
`http://10.65.191.229/api/child/md5/eccbc87e4b5ce2fe28308fd9f2a7baf3`


##
## Answers
#### Q: What does IDOR stand for?
#### A: `Insecure Direct Object Reference`
##
#### Q: What type of privilege escalation are most IDOR cases?
#### A: `horizontal`
##
#### Q: Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children?


#### A: `15`
#### Steps:
* Lest test all user account from 10-20
To check if any of them has 10 Children
* Simply go to Inspect -> Storage -> Local storage
* Change the value of `user_id` each time
- from user 11-14 i see only test users
- user 15 has 15 children

##
### Bonus questions
#### Bonus Task:
 If you want to dive even deeper, use either the base64 or md5 child endpoint and try to find the id_number of the child born on 2019-04-17? 

 #### A: `19`

#### Steps:
* Just check the childs of the user found in previous question
* The id is inside the info menu of the child


##
#### Bonus Task 2 :
 Want to go even further? Using the /parents/vouchers/claim endpoint, find the voucher that is valid on 20 November 2025. Insider information tells you that the voucher was generated exactly on the minute somewhere between 20:00 - 24:00 UTC that day. What is the voucher code? If you want to check your answer, click the hint on the question.

 #### A: `22643e00-c655-11f0-ac99-026ccdf7d769`

#### Steps:
* This one is more difficult
* will use burp-suite for this 

1. First create a script (using AI) to generate a list of UUID for every minute from 20:00 until 24:00 on the 20.11.2025 (240 UUID total)
    * I've added the script to the task folder
2. Go to `http://10.65.191.229/parents/vouchers/claim`, enter anything and capture the request using burp
3. send the request to the intruder
4. highlight the code part with $$
 * {"code":"$$"}
5. Load the list generated by the python script
6. Run the attack
7. Wait until you get a response code of 200
## You completed the room!!!