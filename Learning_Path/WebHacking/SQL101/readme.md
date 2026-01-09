
## Walkthrough of SQL Fundamentals room - THM



## Theory - What will we learn?
* What are databases(including Types)
* Learn about SQL



### What is a database
* Collection of orgenized data, that can be easily accesed and managed

```
#Example:
* database that contains usernames and hashed passwords, and is checked when user accesss a website or application

* Database of social network contains posts/comments/likes etc...

* application like netflix have databases for watching history of users, used to recommend new content
```

### Types of Databases
* There are many, we'll focus on the 2 main ones:
1. Relational databases (Like SQL)
* data is orgenized in formats
    * example: user will contain always(name,email,username,pass)
* data is contained inside tables
    * there are realationships between the tables
2. Non-Relational Databases (No-SQL)
* data is stored in non table format
* used when there are many types of entries and they change between objects
    * example: user's content on facebook


### Tables Rows and Columns
* Lets take for example a Book collection inside a book store
    * When creating the table we'll want to set the columns with the attributes of each book
    * each column has its own data type(strings,integers,floats,dates)

* each row will represent a book
* when adding a book you need to specify all the books attributes


### Keys
1. Primary key 
    * indicates the number of the raw(the book) in the table
    * there is only one primary key in each table
2. Foreign Key
    * Points to another object in another table
    * this is how we creatin relations between 2 tables
    

### What is SQL
* How can the user manage the data base?
* `DBMS - Database Management System`
* This is the interface between the user and the database
    * Examples: 
    * `MySQL` `MongoDB` `Oracle Database` AND `Maria DB`

* SQL acts as the "language" user can talk with the database with
* SQL is short for `Structured Query Language`
#### `Used in relational database`

1. SQL is fast
2. easy to learn and use(Very similar to plain english)
3. Reliable
4. Flexible

## Practical
1. connect to DBMS
```bash
mysql -u $USERNAME -p
#then specify the password
```

#### Basic commands
```bash
#Create database
CREATE DATABASE $database_name;

#List all databases
SHOW DATABASES;
# * There are databases created by defult --->
# [ mysql, information_scheme, performance_scheme and sys ] 

# Select a database
USE $database_name;

# Delete a database
DROP database $database_name;

# Create TABLE
CREATE TABLE $example_table_name (
    $example_column1 $data_type,
    $example_column2 $data_type,
    $example_column3 $data_type
);
# First colume shuld be set with AUTO_INCREMENT and PRIMARY KEY settings
#Example: book_id INT AUTO_INCREMENT PRIMARY KEY,

#List all tables
SHOW TABLES;

#List all columns(attributes) inside a table
DESCRIBE $table_name;

#Update tables columns
ALTER TABLE $table_name
ADD $example_column1 $data_type;

# Delete Table
DROP TABLE $table_name;
```
#### CRUD operations(Create , Read , Update , Delete)
```bash
# Add data into a table
INSERT INTO $TABLE ( $column1, $column2, $column3)
VALUES( $DATA, $DATA, $DATA);

# Read all data in table
SELECT * FROM $TABLE;
# Read only specific columns
SELECT $column1, $column2 FROM $table;

#UPDATE existing row(record)
UPDATE books
SET $column = $data WHERE id = $id; 

#Delete record
DELETE FROM $table WHERE id = $id;
```
#### Clause 
```bash
# Print tables data without duplicates
# like uniq command
SELECT DISTINCT $columns FROM $table;

# Count and print number of occurences
# like uniq -c
SELECT name, COUNT(*) 
FROM $table
GROUP BY $column;

# print data in ascending order
SELECT * FROM $tables ORDER BY $column ASC;
# print data in descending order 
SELECT * FROM $tables ORDER BY $column DESC;

# Filter data
SELECT $column, COUNT(*)
    FROM $table
    GROUP BY $column
    HAVING $column LIKE '$str'

#Operators
#LIKE
SELECT * FROM $table
WHERE $column1 LIKE "%$data%"; 
#AND
SELECT * FROM $table
WHERE $column1 = "$data" AND $column2 = "$data"; 

#OR
WHERE $column1 = "$data" OR $column2 LIKE "$data"; 

#NOT
WHERE NOT $column LIKE "%$data%"

#Between
WHERE 4column BETWEEN 2 AND 4;

= / != / > / <=
```

#### FUNCTIONS
```bash
# printf in sql
SELECT CONCAT( $column1, "bla bla bla", $column2 "bla.") AS $NEW_COLUMN FROM $table;

# group by column, then print all in single line
SELECT $column1, GROUP_CONCAT( $column2 SEPARATOR ", ") AS $new_column
    FROM $table
    GROUP BY $column1;

#print specific number of characters from each row
SELECT SUBSTRING($column, 1, $numOfChars) AS $newColumn FROM $table;

#Get length of string
SELECT LENGTH($column) AS $newColumn FROM $table;

#Return number of records 
SELECT COUNT(*) AS $newColumn

#Sum all values
SELECT SUM($column) AS $newColumn FROM $table;

#return max value
SELECT MAX($column) AS $newColumn FROM $table;
#return min value
SELECT MIN($column) AS $newColumn FROM $table;


```



## You completed the room!!!
