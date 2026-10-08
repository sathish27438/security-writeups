Title: Password reset broken logic

Vulnerability:  Password reset broken logic

Severity: High

Attack Surface: This lab is vulnerable to token validation

What Happened: The forgot password flow generates a reset token for wiener. 
When submitting the new password the server accepts the token 
but does not verify that the token belongs to the username 
in the request. By changing the username parameter to carlos 
while keeping wiener's valid token, an attacker can reset 
carlos's password without knowing his original password.

Payload: change the username field

Impact: Attacker can able to login with other user if they identified the username.

Remediation: The server must cryptographically bind the reset token to the 
username at generation time. When the reset form is submitted 
validate that the token was issued for the exact username in 
the request. Reject any request where the token and username 
do not match.

What I Learned: i learned how to check endpoints and validation where should have to happen

Mistakes I Made: still i have to understand the request and response, then only i can able to modify
