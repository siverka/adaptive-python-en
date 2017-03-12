import re

string = input()
# string = 'aaaabbcaa'
groups = re.findall(r'((\w)\2*)', string)
result = [group[1] + str(len(group[0])) for group in groups]
print(''.join(result))
