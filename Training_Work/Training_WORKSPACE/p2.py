input_no = int(input("Enter no : "))

fact = 1
for i in range(input_no, 1, -1):
    fact *= i

print(fact)
