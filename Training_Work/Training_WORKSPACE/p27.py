lists = [12, 24, 35, 70, 88, 120, 155]

lists = [lists[i]
         for i in range(len(lists)) if i != 0 and i != 2 and i != 4 and i != 6]


print(lists)
