## Walkthrough of TryHackMe - JavaScript Essentials room

#### What is JS?
* Scripting Language
* allows web developers to add interactive features to websites containing HTML and CSS
* Examples: validation, onClick actions, animations etc...



### Variables
* var -> old type, Dont use it today
* let -> New type, scope only inside the scope {}
* const -> Also scope {}, But doesnt allow changing the value

summery ->
`const` is best, if needs to change value use `let`

### Data types
string
* `let name = "Nick";`
* ``` let text = `Hi ${name}`; ```

number
* `let age = 22; let age = 19.99; let age = -5;`

boolean
* `let isLoggedIn = true;`
* `let isAdmin = false;`

null
* `let user = null;`
undefined
* `let x;` #Printing will result undefined(no value)

object (For more complex like array and objects)
* Object example
```JS
const user = {
  name: "Nick",
  age: 22,
  isAdmin: false
};

```
* Array example
```JS
const numbers = [1, 2, 3, 4];
const names = ["Nick", "John"];

```

* Functio example
```JS
function sayHi() {
  console.log("Hi");
}

```

### Loops
for
```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}

```
while
```js
let i = 0;

while (i < 3) {
  console.log(i);
  i++;
}

```
do while

```js
let i = 5;

do {
  console.log(i);
  i++;
} while (i < 3);

```


### Q: What term allows you to run a code block multiple times as long as it is a condition?

### A: `loop`

### Q: What is the code output if the value of x is changed to 10?
```js
let x = 10;
let y = 10;
let result = x + y;
console.log("The result is: " + result);
```

### A: `The result is: 20`

### Q: Is JavaScript a compiled or interpreted language?


### A: `interpreted`

##
#### Integrating JavaScript in HTML
### Internal JS

```js
    <h1>Addition of Two Numbers</h1>
    <p id="result"></p>

    <script>
        let x = 5;
        let y = 10;
        let result = x + y;
        document.getElementById("result").innerHTML = "The result is: " + result;
    </script>
```
### External JS
* create a .js file
```js
let x = 5;
let y = 10;
let result = x + y;
document.getElementById("result").innerHTML = "The result is: " + result;
```

* call the .js file from the html file
```js

<body>
    <h1>Addition of Two Numbers</h1>
    <p id="result"></p>

    <!-- Link to the external JS file -->
    <script src="script.js"></script>

```
* See? Same output as before only this time the code is orgenized


### Q: Which type of JavaScript integration places the code directly within the HTML document?

### A: `Internal`

### Q: Which method is better for reusing JS across multiple web pages?

### A: `External`

### Q: What is the name of the external JS file that is being called by external_test.html?
* open the External JS file
* right click -> inspect ->

`<script src="thm_external.js"></script>`
### A: `thm_external.js`

### Q: What attribute links an external JS file in the script tag?

### A: `src`

##
### In-Built functions
`alert` --> Popup box that stops the code until OK button is presed
`prompt` --> Popup box that allows user input
`confirm` --> Popup box that ask cancel or Ok, return true/false

```js
name = prompt("What is your name?");
    alert("Hello " + name);
```

### Q: In the file invoice.html, how many times does the code show the alert Hacked?

```js
 for (let i = 0; i < 5; i++) {
            alert("Hacked");
 }
```

### A: `5`

### Q: Which of the JS interactive elements should be used to display a dialogue box that asks the user for input?


### A: `prompt`

### Q: If the user enters Tesla, what value is stored in the carName= prompt("What is your car name?")? in the carName variable?

### A: `Tesla`

### Q: What is the message displayed if you enter the age less than 18?

### A: `You are a minor.`

### Q: What is the password for the user admin?
* Lets inspect login.html
```js
 if (username === "admin" && password === "ComplexPassword") {
            document.write("You are successfully authenticated!");
```
* Enter this credentials to log in
### A: `ComplexPassword`


##
### Obfuscation in JS
* use [This site](https://codebeautify.org/javascript-obfuscator) to Encrypt
* use [This site](https://obf-io.deobfuscate.io/) to Decrypt

### Q:What is the alert message shown after running the file hello.html?

### A: `Welcome to THM`

### Q:What is the value of the age variable in the following obfuscated code snippet?
age=0x1*0x247e+0x35*-0x2e+-0x1ae3;

* Use the decrypter site to see the real age

### A: `21`

##
### How to write secure code in JS?
* Gold rule -> If the code is written on the client side, its not a secret

* Dont relay on Client size validation -> Can be manipulated
* Dont use untrusted libraries
* Dont insert private tokens/credentials/api keys inside the JS code


### Q: Is it a good practice to blindly include JS in your code from any source (yea/nay)?

### A: `nay`

## You completed the room!!!