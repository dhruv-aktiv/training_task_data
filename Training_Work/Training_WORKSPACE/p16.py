import random

start_no = 1
end_no = 1000

lists = [i for i in random.sample(
    range(start_no, end_no + 1), 5) if i % 5 == 0 and i % 7 == 0]

print(lists)

# work need
