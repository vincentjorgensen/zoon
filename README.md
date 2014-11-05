zoon
====
Lightweight Application Launch Utility for AWS
----------------------------------------------

Usage:
------
(Note, this is proposed usage)
zoon.py <engine> [engine\_args] <action> [action\_args]
e.g.
zoon.py consul create LTarquiniusCollatinus --aws --size=5 --region=us-east-1 --az=us-east-1c --az=us-east-1d --az-us-east-1c --sg=praetor

Currently, the AWS Security Group must already exist.


- --aws Defaults to True
- --region=region Defaults to us-east-1
- --az=AZ Defaults to us-east-1c, multiple allowed, instantiates in round-robin fashion
- --sg=sg No default, optional
- --vpc Defaults to false

.zoonrc
-------
Sits in Home Directory, for example: $HOME/.zoonrc

default\_environment: dev
environments:
\- dev: : Dev
  username: spongebobsquarepants
  aws\_access\_key\_id: 'AKIA...'
  aws\_secret\_access\_key: '...'
