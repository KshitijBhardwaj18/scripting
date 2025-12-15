import os
import glob
import json

# result = []

# for path in glob.glob("data/logs/json/*"):
#     filename = os.path.basename(path)
#     print(filename)
#     with open(path, "r") as l:
#         for lg in l:
#             log = json.loads(lg)
#             print(log)
#             if (log.get('status') == "error" or "ERROR"):
#                 result.append(log)

# print(result)


## V1

# def iter_error_logs(log_dir):

#     for path in glob.glob(os.path.join(log_dir,"*")):
#         with open(path,"r") as f:
#             for l in f:
#                 try:
#                     log = json.loads(l)
#                 except json.JSONDecodeError:
#                     continue

#                 status = log.get('status')
#                 if isinstance(status,str) and status.lower() == "error":
#                     yield log


# if __name__ == "__main__":
#     LOG_DIR = "data/logs/json"

#     for error_logs in iter_error_logs(LOG_DIR):
#         print(error_logs)


## V2

def iter_error_logs(LOG_DIR):

    for path in glob.glob(os.path.join(LOG_DIR,"*")):
        with open(path, "r") as f:
            try:
                log = json.load(f)
                if isinstance(log,list):
                    for lg in log:
                        status = lg.get("status")
                        if isinstance(status,str) and status.lower() == "error":
                            yield lg
            except json.JSONDecodeError:
                f.seek(0)
                for lg in f:
                    try:
                        log = json.loads(lg)
                        status = log.get("status")
                        if isinstance(status,str) and status.lower() == "error":
                            yield lg
                    except json.JSONDecodeError:
                        continue

                    



if __name__ == "__main__":
    LOG_DIR = "data/logs/json"

    for error_logs in iter_error_logs(LOG_DIR):
        print(error_logs)

                    

