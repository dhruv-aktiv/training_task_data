import math

# map practice

# map(function, iterable(s)) #syntax

# do a square of elements
lists = [1, 2, 3, 4, 5, 6, 7]
square_no = map(lambda no: no ** 2, lists)

print(list(square_no))

# convert to upper case all elements

string_it = ["processing", "strings", "with", "map"]
print(list(map(str.upper, string_it)))


# factorial of each number
nos = [1, 2, 3, 4, 5, 6, 7]
fact_no = list(map(math.factorial, nos))
print(fact_no)
