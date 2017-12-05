About
=====

HTTPLang is a scripting language that makes writing HTTP request routines simpler.

Current Version
===============

0.2.0

What could I use it for?
====

- Testing APIs
- Web Scraping
-


Installation
====
* Clone the repo
* Run `python setup.py install`

Usage
===
`httplang l<file.http>`

Documentation
=============

Important Note
--------------

HTTPLang is very strict about things like spaces. Make sure that your code matches the spacing and what not exactly as shown in the examples. If not there will be errors.

Examples
--------


```

set URL "http://google.com"
do GET "/
show RESPONSE

``` 

```
set URL "http://google.com"
label "loop"
do GET /
show STATUS
goto "label"

```

```

set URL "http://somesite.com"
set POSTDATA "username=myUsername&password=myPassword is this"
do POST "/login"
set COOKIE TMPCOOKIE
do GET "/usercp"

```

