

lists = list(map(int, input().split(',')))

lists = [ele**2 for ele in lists if ele % 2 != 0]

print(*lists, sep=",")
