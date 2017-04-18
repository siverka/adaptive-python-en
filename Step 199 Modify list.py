def modify_list(l):
    l[:] = [x//2 for x in l if x % 2 == 0]
