input_no = int(input("Enter no : "))

dicts = {}

for i in range(input_no):
    dicts[i + 1] = (i + 1) * (i + 1)

print(dicts)
