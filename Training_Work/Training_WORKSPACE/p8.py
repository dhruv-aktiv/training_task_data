
no_of_transaction = int(input("Enter no of traction you want to enter :"))

transactions = []
for i in range(no_of_transaction):
    mod, amt = input().split(' ')
    transactions.append((mod, int(amt)))


total_amt = 0

for i in range(no_of_transaction):
    mod, amt = transactions[i]
    if mod.upper() == 'D':
        total_amt = total_amt + amt
    else:
        total_amt = total_amt - amt


print(abs(total_amt))
