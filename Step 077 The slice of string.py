with open('Input step 077 The slice of string.txt', 'r') as file:
    s = file.readline().strip()
    a, b, c, d = (int(i) for i in file.readline().strip().split())
    print(s[a: b + 1], s[c: d + 1])
