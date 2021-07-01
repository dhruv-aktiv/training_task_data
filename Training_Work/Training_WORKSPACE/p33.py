
no = 6
for row in range(no, 0, -1):
    for k in range(no - row):
        print(" ", end="")
    for col in range(row):
        print("*", end=" ")
    print("\n")
