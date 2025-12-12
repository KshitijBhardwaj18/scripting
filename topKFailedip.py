import os
import glob
import re
import heapq

def top_k_failed_ips(k):
    pattern = re.compile(r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<time>.*?)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+)')
    result = []
    fails = {}

    for path in glob.glob("data/logs/nginx/*.log"):
        logfile = os.path.basename(path)
        with open(path,"r") as f:
            for log in f:
                m = pattern.match(log)
                if not m:
                    continue
                ip = m.group("ip")
                status = m.group("status")
                if status == "404":
                    fails[ip] = fails.get(ip,0) + 1
    
    return heapq.nlargest(k, fails.items(), key = lambda x : x[1])

ans = top_k_failed_ips(3)

print(ans)
    


