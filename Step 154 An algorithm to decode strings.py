from re import sub

string = sub(r'(\d+)(\w)', lambda x: x.group(2) * int(x.group(1)), input())
print(string)
