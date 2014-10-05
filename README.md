zoon
====
Lightweight Application Launch Utility
--------------------------------------

Usage:
------
(Note, this is proposed usage)
zoon.py <engine> [engine\_args] <action> [action\_args]
e.g.
zoon.py nginx create webapp1 --aws --size=3 --region=us-east-1 --az=us-east-1c --sg=webapp1

Currently, the AWS Security Group must already exist. I plan to make it such that it creates it if it doesn't exist.


- --aws Defaults to True
- --region region Defaults to us-east-1
- --az sg Defaults
- --sg sg No default, optional
- --vpc Defaults to false
