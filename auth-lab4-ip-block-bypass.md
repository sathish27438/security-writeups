Title: Broken brute-force protection, IP block

Vulnerability: Brute-Force

Severity: High

Attack Surface:
This lab is vulnerable to username enumeration and password brute-force attacks

What Happened:
The application blocks an IP after 3 consecutive failed login 
attempts. However if a valid login is made before reaching the 
limit, the counter resets. By interleaving valid credentials 
(wiener/peter) every 2 attempts, the block is never triggered 
and the attacker can brute force the target account indefinitely.

Payload:
username = LIST & password = LIST

Impact:
- Rate limit by account not just IP address
- Implement exponential backoff — increasing lockout time per failure
- Block based on username not just IP to prevent IP rotation bypass

Remediation:
• Trigger a CAPTCHA challenge after a small number of consecutive failed login attempts (e.g., three failures) to disrupt automated tools



What I Learned:
i learned about how brute force attacks works and i learned how to use intruder in the burpsuite and i learned how IP blocks works in the backend .

Mistakes I Made:
still i am lacking how to use burp intruder in the burpsuite like payload type selection and this time i understood pitchfork attack and sniper attack