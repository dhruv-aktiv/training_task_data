no_of_lines = int(input("How many lines you want to enter :"))

lines = []

lines = [str(input()).upper() for i in range(no_of_lines)]

# lines = [line.upper() for line in lines]

print("\n".join(lines))
