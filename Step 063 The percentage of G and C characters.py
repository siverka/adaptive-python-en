import re

string = input()
f = re.findall(r'c|g', string, re.IGNORECASE)
print(100 * len(f) / len(string))
