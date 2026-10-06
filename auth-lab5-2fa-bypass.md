Title: 2FA simple bypass

Vulnerability: Broken Authentication or 2FA Bypass

Severity: High

Attack Surface: This lab is vulnerable to 2FA and the enpoint is /my-account

What Happened: if the user authenticate and if the receive auth code and the /my-account does not do any validation so the user can easily bypass the 2FA from /login to /my-account.

Payload: change the enpoint /my-account

Impact: Attacker can able to login with other user if they have credentials of users even if 2FA is enabled.

Remediation: The server must track whether the user has completed the 2FA 
step before granting access to authenticated pages. Store the 
2FA completion state in the session and validate it on every 
request to protected endpoints.

What I Learned: i learned how the connection state works and where we have the check.

Mistakes I Made: still i have to understand the request and response, then only i can able to modify
