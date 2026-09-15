Title: Visible error-based SQL injection

Vulnerability: SQL Injection (SQLi)

Severity: High

Attack Surface: The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie

What Happened:
step 1: identifying the ATTACK surface, after the we validate the attack surface by passing condition operators here the payload is ' AND CAST() and successfully returning the error page(internal server error).

step 2: we have successfully able to identify the attack surface and for next we have craft our payload here the payload we have used is ' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)-- and it is successfully identified the PASSWORDS.



Payload:' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--


impact: An attacker can extract all usernames and passwords from the database giving full account takeover of any user including administrators.

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: i have learned the how to craft the based on the context and based on the databases types and here i have new function called CAST which is helps to change the data types.

Mistakes I Made: i have lots of mistakes here like crafting payload based on the databases types and concentation mistakes and  i mostly rely on AI only, still i have to understand blind sqli completely.