shapes = {'1': 'square', '2': 'circle', '3': 'triangle', '4': 'rhombus'}
n = input()
if n in shapes:
    print('You have chosen a', shapes[n])
else:
    print('There is no such shape!')
