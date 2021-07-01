# check if the file exist only then delete the file
import os
file_name = 'test_file.txt'

if os.path.exists(file_name):
    os.remove(file_name)
else:
    print("The file does not exist")
