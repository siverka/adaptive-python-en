string = input()
d = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
output = [d[string[2*i:2*i+2]] for i in range(len(string)//2)]
print(''.join(output))
