lists = [12, 24, 35, 70, 88, 120, 155]

lists = [lists[i] for i in range(len(lists)) if i != 0 if i != 4 if i != 5]

print(lists)
