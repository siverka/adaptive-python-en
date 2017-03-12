import re


def replace(matchobj):
    return matchobj.groups()[1] + str(len(matchobj.groups()[0]))

string = input()
string = re.sub(r'((\w)\2*)', replace, string)
print(string)
