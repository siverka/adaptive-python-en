word = input()
output = [w for i, w in enumerate(word) if i % 2 == 0]
print(''.join(output))
