import re
with open('./blocklist.xml') as f:
    for line in f.readlines():
        if re.search(r'id=\"[a-zA-Z0-9._-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+\"', line) is not None:
            print(line)
