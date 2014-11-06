zoon
====
Lightweight Application Launch Utility for AWS
----------------------------------------------
Python utility for automating many AWS tasks, like CloudFront.

Requires: pyyaml, boto

Written by: [Vincent Jørgensen](mailto:vincent_dot_jorgensen_at_gmail_dot_com), 2014
Freely distributable via the [MIT License](http://choosealicense.com/licenses/mit/).

On the name 'zoon', and it's pronunciation
---------
"zoon" is an English transliteration of the Greek "ζῷον", meaning "animal, living thing." In Ancient Greek, in would have been approximately pronounced like &lt;sdoooe-on&gt;. One may refer to this project as "zoon, rhymes with zoom", "zoon, like 'so on' but with a 'z' sound instead of an 's'", or anything closely approximating the Greek.

Usage:
------
zoon.py [-h] [optional args] &lt;engine&gt; [engine\_args] 
e.g.
**zoon.py** *consul* create LTarquiniusCollatinus --aws --size=5 --region=us-east-1 --az=us-east-1c --az=us-east-1d --az-us-east-1c --sg=praetor


.zoonrc
--------
Located in `$HOME/.zoonrc`
```
default_environment: dev
environments:
  - dev: Dev
    username: spongebobsquarepants
    aws_access_key_id: 'AKIA...'
    aws_secret_access_key: '...'
```


> Written with [StackEdit](https://stackedit.io/).
