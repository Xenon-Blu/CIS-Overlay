import time
from time import strftime
info = {}
with open("info.txt") as f:
    for line in f:
        name, item = line.partition("=")[::2]
        info[name.strip()] = str(item.strip())
print(info["studentid"])
print(info["courseid"])
print(info["professor"])
while True:
    print (" " + strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)
