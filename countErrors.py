import os
import glob
"""
os.listdir os.path.join os.getcwd()


"""

errors = {}



# for filename in os.listdir("data/logs"):
#     log_dir = "data/logs"
#     logpath = os.path.join(log_dir,filename)
#     count = 0
  
#     with open(logpath, "r") as f:
#         for line in f:
#             if "ERROR" in line:
#                 count+=1
#     errors[filename] = count

for path in glob.glob("data/logs/**/*.log",recursive=True):
    filename = os.path.basename(path)
    with open(path,"r") as f:
        errors[filename] = sum(1 for line in f if "ERROR" in line)


print(errors)


    
