zoon
====
Lightweight Application Launch Utility for AWS
----------------------------------------------

Usage:
------
(Note, this is proposed usage)
zoon.py <engine> [engine\_args] <action> [action\_args]
e.g.
zoon.py consul create LTarquiniusCollatinus --aws --size=3 --region=us-east-1 --az=us-east-1c --sg=praetor

Currently, the AWS Security Group must already exist. I plan to make it such that it creates it if it doesn't exist.


- --aws Defaults to True
- --region region Defaults to us-east-1
- --az AZ defaults to us-east-1c
- --sg sg No default, optional
- --vpc Defaults to false
