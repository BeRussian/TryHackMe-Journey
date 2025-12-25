## Walkthrough of Day 20 - Race Conditions - Toy to The World 



## Theory - What will we learn?
* Understand what race conditions are and how they can affect web applications.
* Learn how to identify and exploit race conditions in web requests.
* How concurrent requests can manipulate stock or transaction values
* Explore simple mitigation techniques to prevent race condition vulnerabilities



### What are race conditions?
* Happens when 2 actions take place in the exacts same time
* Results depands on the order they finish
* happens when multiple users or automated requests simultaneously access or modify shared resources

### Types of Race Conditions
* Time-of-Check to Time-of-Use (TOCTOU)
    * 2 Users buy the same "Last item" at the same time, because stock was checked before it was updated
* Shared resource
    * Think of two cashiers updating the same inventory spreadsheet at once
    * and one overwrites the other’s work.
* Atomicity violation
    * a payment is recorded, but the order confirmation fails because another request interrupts the process.


### Practical
basic nmap gave us this results
```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

```
Lets connect to the http web-application
we got valid credentials from the room
username `attacker`
password `attacker@123`

We see store interface, we can check out items
Lets try to exploit the Race Conditions vulnerability

1. Open burp
2. sent the `/process_checkout` POST request to the repeter
3. Create a group and duplicate by at least 10
4. Select send group in parallel(last-byte sync)
5. Send it!!!
6. You should see the first flag

### Flag --->
### THM{WINNER_OF_R@CE007}

Lets do the same only with the second toy(Bunny plush)
1. Buy and checkout the `Bunny plush`
2. Send to intruder-> Create a group and duplicate
3. send in parallel
### Flag --->
### THM{WINNER_OF_Bunny_R@ce}


## You completed the room!!!