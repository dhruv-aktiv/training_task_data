no = 6

for row in range(no):
    for k in range(no - row + 1):
        print(" ", end=" ")
    for col in range(row + 1):
        print("*", end=" ")
    print("\n")
