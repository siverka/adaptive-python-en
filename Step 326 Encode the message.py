string = input()
d = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
output = [d[w] for i, w in enumerate(string)]
print(''.join(output))
