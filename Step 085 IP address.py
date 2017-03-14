address = input().split('.')
print('YES' if len(address) == 4 and
               all(map(lambda i: i.isdigit() and 0 <= int(i) <= 255, address))
      else 'NO')
