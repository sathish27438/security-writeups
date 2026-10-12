Title: Insecure direct object references

Vulnerability: IDOR/BOLA

Severity: High

Attack Surface: This lab is vulnerable to IDOR (/download-transcript/2.txt)

What Happened: In this lab we have try to download the transcript and in that endpoint it use predictable numbers to retrive the files from the server.
with changing the value from 2 to 1 we can see the others chat and there is no proper authentication mechanism to protect. with we can able to identify 
the password of carlos and resolved the lab.

Payload: = decrementing the value of filesystem numbers. 

Impact: An attacker can access any user's chat transcript by 
incrementing the file ID. This exposes sensitive conversations 
and in this case leaked the credentials of another user.

Remediation: Validate that the authenticated user owns the requested 
resource before serving it. Never use sequential predictable 
IDs for sensitive resources. Use UUIDs or indirect references 
that are mapped server-side to the actual resource.

What I Learned: i learned how to exploit the IDOR vulnerability without burpsuite

Mistakes I Made: I feel like I am forgetting SQLi concepts from not practicing 
them recently. Need to revisit blind SQLi and UNION attacks.
