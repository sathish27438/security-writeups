Title: SQL Injection — Authentication Bypass via Login Form

sql injection Severity: High 

Attack Surface: Login form 

What Happened: 
in the login form there is no input validation or any defensive mechanism, so when the user inserting the payload administrator'-- in the username, they can able to bypass login check and able to login as an administrator Payload: administrator'--

Impact: 
Full control over the application
Access to all user data including passwords and personal information
Ability to modify, delete, or exfiltrate data
Potential to pivot to the underlying server

Remediation: Use parameterized queries (prepared statements). Never concatenate user input directly into SQL queries. The query structure must be defined first and user input passed separately as a parameter so the database never treats it as executable code.

What I Learned:
I learned that commenting out the password check with -- 
completely removes authentication. The key insight is that 
the database executes whatever SQL it receives — it has no 
concept of "this should be a login check."

Mistakes I Made:
I jumped to explaining the payload before writing out the 
original query structure. I also skipped the Learned and 
Mistakes sections in my first draft of this writeup.
