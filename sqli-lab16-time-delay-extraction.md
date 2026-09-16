Title: Blind SQL injection with time delays and information retrieval

Vulnerability: SQL Injection (SQLi)

Severity: High

Attack Surface: The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie

What Happened:
step 1: identifying the ATTACK surface, after the we validate the attack surface by passing condition operators here the payload is ' AND '||pg_sleep(10)-- and it is delaying the request for 10 sec later and we can identifying that sqli possible.

Step 2: we craft our payload with CASE function with time delay which is helping us to identify sqli is possible

Step 3: writing python script for both identifying the length of the password and retrive the password.


Payload:'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,1,1)='a')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--


impact: Time-based blind SQLi confirms the vulnerability exists and 
allows an attacker to extract data character by character 
by measuring response delays, even when no output is visible.

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: i have learned the how to craft the based on the context and based on the databases types and i understand how time delays works and here i learned ; should be encoded because it will separate the cookie values.

Mistakes I Made: i have lots of mistakes here like crafting payload based on the databases types and concentation mistakes and  i mostly rely on AI only, still i have to understand blind sqli completely.