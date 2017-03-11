def healthy_sleep(a, b, h):
    if h < a:
        print('Deficiency')
    elif h > b:
        print('Excess')
    else:
        print('Normal')


healthy_sleep(int(input()), int(input()), int(input()))
# healthy_sleep(6, 10, 8)  # N
# healthy_sleep(7, 9, 10)  # E
# healthy_sleep(7, 9, 2)  # D
