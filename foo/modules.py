import json
import re

# Useful modules

x = ' { "a" : 1, "b" : 2}'
o = json.loads(x)
print(o["a"])

text = "Hello, World!"
match = re.search("Hello(.*)", text)
if match:
    print(match.group(1))
