directions = {'1': 'move up', '2': 'move down', '3': 'move left', '4': 'move right', '0': 'do not move'}
n = input()
print(directions[n] if n in directions else 'error!')
