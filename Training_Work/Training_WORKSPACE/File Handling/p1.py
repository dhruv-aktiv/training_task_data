
# line by line print file content
file_name = 'test_file.txt'
with open(file_name) as file:
    for line in file:
        print(line)

# line by line print file content with line number
input = open(file_name, 'r')
for i, line in enumerate(input, start=1):
    print(f"Line Number {i} : {line}")
