lists = []

start_no, end_no = input(
    "Enter starting number and ending number with comma(,) : ").split(',')
start_no = int(start_no)
end_no = int(end_no)

div_no = 7
multi_no = 5
delimeter = ","
lists = [no for no in range(start_no, end_no) if no %
         div_no == 0 and no % multi_no != 0]

print(*lists, sep=delimeter)
