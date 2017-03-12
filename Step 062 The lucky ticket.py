ticket = [int(i) for i in input()]
print("Lucky" if sum(ticket[:3]) == sum(ticket[3:]) else 'Regular')
