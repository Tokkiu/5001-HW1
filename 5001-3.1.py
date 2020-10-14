import re
with open('./blocklist.xml') as f:
    for line in f.readlines():
        if re.search(r'<emItem blockID="[i|g].*?[0-9]', line) is not None:
            print(line)
