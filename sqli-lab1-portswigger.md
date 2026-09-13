Title: SQL Injection in Category Filter

Vulnerability: SQL Injection (SQLi)
Severity: High

Attack Surface:
GET /filter?category= parameter

What Happened:
The category parameter passes user input directly into a SQL
query without sanitization. Injecting a single quote causes
a 500 error confirming the input reaches the database
unfiltered. Using the payload ' OR '1'='1'-- bypasses the
WHERE clause entirely and comments out the released=1
restriction.

Payload:
' OR '1'='1'--

Impact:
An attacker can bypass product visibility restrictions and
retrieve data that is not intended to be public. In a more
complex database this technique can be extended to extract
usernames, passwords, and other sensitive data from any
table in the database.

Remediation:
Use parameterized queries (prepared statements). Never
concatenate user input directly into SQL queries. The query
structure must be defined first and user input passed
separately as a parameter so the database never treats it
as executable code.


What I Learned:
By injecting a single quote, an attacker can observe how 
the database responds to broken syntax. If the app returns 
a 500 error, the input is reaching the SQL query unfiltered. 
From there, an attacker can manipulate the query logic using 
OR conditions to bypass filters and retrieve hidden data.

Mistakes I Made:
I used ' OR '1'='1= as my first payload which was incorrect. 
The = at the end broke the query wrongly. The correct payload 
is ' OR '1'='1'-- because the -- comments out the rest of 
the query so the database ignores everything after it.
