strs = input("Enter string :")

upper_cnt = 0
lower_cnt = 0
for i in range(len(strs)):
    if strs[i].isupper():
        upper_cnt += 1
    else:
        lower_cnt += 1

print("UPPER CASE %d" % upper_cnt)
print(f"LOWER CASE {lower_cnt}")
