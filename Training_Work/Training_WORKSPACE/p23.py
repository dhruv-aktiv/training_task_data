lists = [12, 24, 35, 24, 88, 120, 155]

remove_ele = 24

lists = [lists[i] for i in range(len(lists)) if lists[i] != remove_ele]

print(lists)
