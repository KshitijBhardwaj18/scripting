import os
import glob

ips = set()
requestPerIp = {}
notFoundResponse = {}


for path in glob.glob("data/logs/nginx/*.log"):
    with open(path,'r') as f:
        for line in f:
            ip = line.split(" ")[0]
            if "404" == line.split(" ")[8]:  notFoundResponse[ip] = notFoundResponse.get(ip,0) + 1
            ips.add(ip)
            requestPerIp[ip] = requestPerIp.get(ip,0) + 1


print(f"Ip addressed : {ips}")

print(f"Requests per ip : {requestPerIp}")

print(f"Not found responses per ip: {notFoundResponse}")

"""
Regex crash course
1.) Character classes and shorthands

\d digit \w word \s whitespace \D not a digit \W not a word \S not a whitespace

eg.
date: 2004-09-25
regex \d{4}-\d{2}-\d{2}

2.) Quantifiers
* 0 or more 
+ 1 or more
? 0 or 1

eg: match url path



"""