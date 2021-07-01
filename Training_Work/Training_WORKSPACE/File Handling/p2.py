
# writing in file
file_name = 'test_file.txt'

contents = {"aa": 12, "bb": 21}
with open(file_name, "w+") as file:
    file.write(str(contents))
