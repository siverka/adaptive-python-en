lst = input().split()
x = input()
indxes = [i for i in range(len(lst)) if lst[i] == x]
if indxes:
    print(*indxes)
else:
    print("Missing")
