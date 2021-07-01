import random

start_no = 0
end_no = 10

lists = [i for i in range(random.randrange(
    start_no, end_no + 1)) if i % 5 == 0 and i % 7 == 0]

print(lists)
