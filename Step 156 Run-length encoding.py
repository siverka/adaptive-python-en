from re import sub

def encode(matchobj):
    return str(len(matchobj.group(0))) + matchobj.group(0)[0]

string = input()
string = sub(r'(\w)\1+', encode, string)
print(string)
