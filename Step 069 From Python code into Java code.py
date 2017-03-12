import re


def replace(matchobj):
    return matchobj.group(matchobj.lastindex).upper()


string = input()
string = re.sub(r'_(\w)|^(\w)', replace, string.lower())
print(string)
