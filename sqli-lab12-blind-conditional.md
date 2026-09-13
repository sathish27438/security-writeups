Title: Blind SQL injection with conditional responses

Vulnerability: SQL Injection (SQLi)

Severity: High

Attack Surface: The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie

What Happened:
step 1: identifying the ATTACK surface, after the we validate the attack surface by passing condition operators here the payload is ' AND '1'='1 and successfully returning the welcome page
step 2: we have successfully able to identify the attack surface and for next we have craft our payload here the payload we have used is ' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a and it is successfully identified the character.
step3: we have created our custom python script to automate this and then we able to identified the password and lab is also resolved.

Payload: ' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a

impact: An attacker can extract all usernames and passwords from the database giving full account takeover of any user including administrators.

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned: i have learned the how to craft the based on the context and here i have new function called substring which is helps to extract the character.

Mistakes I Made: i have lots of mistakes here like 'AND '1'='1 without space here and the payload it is not working and for scripts i mostly rely on AI only, still i have to understand blind sqli completely and writing scripting also.
