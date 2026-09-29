Title: Username enumeration via response timing

Vulnerability: Brute-Force

Severity: High

Attack Surface:
This lab is vulnerable to username enumeration and password brute-force attacks

What Happened:
The application returns "Invalid username or password." with 
response time is showing high value because if username is valid, it is trying to check the password because of tit is showing high response value with that we can able to identify the valid username and with 302 response code we could able to identify the password.

Payload:
username = LIST & password = LIST

Impact:
if an attacker able to identifying the password and username of administrator, they could take over the application.

Remediation:
• Do not trust the client-supplied XFF header.
• Configure your proxy to strip the header and create a fresh one using the actual connecting socket IP ($remote_addr).


What I Learned:
i learned about how brute force attacks works and i learned how to use intruder in the burpsuite and i learned new thing xff header .

Mistakes I Made:
still i am lacking how to use burp intruder in the burpsuite like payload type selection