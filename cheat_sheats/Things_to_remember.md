## sqli 
## NOTE; -- cookie separator when we sending the payload it should be encoded ;=value(%3B)
Can you see query results on page?
├── YES → use UNION attack
└── NO (blind)
    ├── Does app behave differently true/false?
    │   └── YES → use AND with SUBSTRING (boolean blind)
    ├── Does app show errors?
    │   └── YES → use CAST (error based)
    └── Nothing works?
        └── use time delays (SLEEP/pg_sleep)