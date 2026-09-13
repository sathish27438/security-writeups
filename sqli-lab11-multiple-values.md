Title : SQL injection UNION attack, retrieving multiple values in a single column

Vulnerability: SQL injection

Severity: High

Attack Surface: SQL injection vulnerability in the product category filter

What Happened: 
SQL injection vulnerability in the product category filter and in this we have to identify of the administrator password from the table of users. issue : only one column is returning text so, we have ,make payload to returning single column for we sed the || concatenation operator to combine username and password into a single column separated by ~ character.


Payload : ' UNION SELECT NULL, username ||'~'|| password from users--;

impact: 
Knowing the number of columns is the first step in a UNION attack. Without this an attacker cannot extract data. This information allows an attacker to build further payloads to dump tables, credentials, and sensitive data from the database.

Remediation: 
Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code

What i learned: 
In this lab the table and column names were provided. In real world targets I would need to enumerate them first using information_schema.tables and information_schema.columns before extracting data.

Mistakes I Made: i had to make trail and error to get the info of columns
