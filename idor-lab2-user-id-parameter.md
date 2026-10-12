Title: User ID controlled by request parameter

Vulnerability: IDOR/BOLA

Severity: High

Attack Surface: This lab is vulnerable to IDOR and parameter is id= <username>

What Happened: In this lab, when the user authenticated it will show the username in the id parameter and it is not having proper access control
and if the attacker change the user id to known username attacker can able to access user account.

Payload: = changing the username in the id parameter.

Impact: An attacker can access admin account by the user-id parameter and take over the control of application.

Remediation: Validate that the authenticated user owns the requested resource before serving it. Never use sequential predictable IDs for sensitive resources. Use UUIDs or indirect references that are mapped server-side to the actual resource.

What I Learned: i learned how to exploit the IDOR vulnerability without burpsuite

Mistakes I Made: No significant mistakes — the vulnerability was straightforward 
to identify from the URL parameter.
