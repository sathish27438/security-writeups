Title: Username enumeration via different responses

Vulnerability: Brute-Force
Severity: High

Attack Surface:
This lab is vulnerable to username enumeration and password brute-force attacks

What Happened:
we have tried brute force attack on username and password parameters in login endpoint and with content-length value we can able to identify the username and later we have tried brute force attack on password enpoint and with the 302 response code we can able to identifying the password for the username.
The application returns "Invalid username" for wrong usernames 
and "Incorrect password" for valid usernames with wrong passwords. 
This difference allowed username enumeration.

Payload:
username = LIST & password = LIST

Impact:
if an attacker able to identifying the password and username of administrator, they could take over the application.

Remediation:
put rate limiting like after three attempt, they should have to lock the account for few hours and they should not let the user to know about whether username or password is right in the response page.


What I Learned:
i learned about how brute force attacks works and i learned how to use intruder in the burpsuite.

Mistakes I Made:
still i am lacking how to use burp intruder in the burpsuite like payload type selection