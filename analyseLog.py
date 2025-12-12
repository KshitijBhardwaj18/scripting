import os
import glob
import re

ips = set()
requestPerIp = {}
notFoundResponse = {}


### Simpler iterative code, Can get trapped in edge cases


# for path in glob.glob("data/logs/nginx/*.log"):
#     with open(path,'r') as f:
#         for line in f:
#             ip = line.split(" ")[0]
#             if "404" == line.split(" ")[8]:  notFoundResponse[ip] = notFoundResponse.get(ip,0) + 1
#             ips.add(ip)
#             requestPerIp[ip] = requestPerIp.get(ip,0) + 1


## regex version
pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<time>.*?)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)'
)

for path in glob.glob("data/logs/nginx/*.log"):
    filename = os.path.basename(path)
    with open(path,"r") as f:
        for log in f:
            m = pattern.match(log)
            if not m:
                continue
            ip = m.group("ip")
            ips.add(ip)
            status = m.group('status')
            requestPerIp[ip] = requestPerIp.get(ip,0) + 1
            if status == "404":
                notFoundResponse[ip] = notFoundResponse.get(ip,0) + 1


print(f"Ip addresses : {ips}")

print(f"Requests per ip : {requestPerIp}")

print(f"Not found responses per ip: {notFoundResponse}")



# Regex crash course
# 1.) Character classes and shorthands

# \d digit \w word \s whitespace \D not a digit \W not a word \S not a whitespace

# eg.
# date: 2004-09-25
# regex \d{4}-\d{2}-\d{2}

# 2.) Quantifiers
# * 0 or more 
# + 1 or more
# ? 0 or 1

# eg: match url path
# /[\w\-\/]+

# 3.) Capture Groups 
# help group the certain patters. below is the regex patter for tracking the 
# ^(\d{3}(\.\d{3}){3})

# 4.)Not capture groups (?:)
# ^(?:\d{3}(?:\.\d{3}){3})

# 5.)Alternation (GET|POST)

# 6.)Anchors ^ and $ these marks the start and the end of the lines

# 7.) Greedy vs Non Greedy ?
# greedy "(.+)"  "(.+?)"

# 8.) [] this defines a character set 
# eg email regex = [\w\.-]+@[\w\.-]+\.\w+

# important patterns url

# https?:\/\/[\w\.-]+(:?\/[\w\.-]*)*

