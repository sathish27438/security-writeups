Title: Username enumeration via subtly different responses

Vulnerability: Brute-Force

Severity: High

Attack Surface:
This lab is vulnerable to username enumeration and password brute-force attacks

What Happened:
The application returns "Invalid username or password." with 
a period for invalid usernames. For valid usernames it returns 
"Invalid username or password" without a period. This subtle 
difference allowed username enumeration.
The application returns "Invalid username or password" without period for wrong usernames 
and "Invalid username or password" for valid usernames with wrong passwords. 
This difference allowed username enumeration.

Payload:
username = LIST & password = LIST

Impact:
if an attacker able to identifying the password and username of administrator, they could take over the application.

Remediation:
put rate limiting like after three attempt, they should have to lock the account for few hours and they should not let the user to know about whether username or password is right in the response page and response should be same for all events.


What I Learned:
i learned about how brute force attacks works and i learned how to use intruder in the burpsuite and i learned new thing grep-extractor on burp suite.

Mistakes I Made:
still i am lacking how to use burp intruder in the burpsuite like payload type selection