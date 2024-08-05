amountDue =50
insertTotal=0
coins=[25, 10, 5]
while amountDue>0 :
    print("Amount Due:",amountDue)
    coinInsert=int(input("Insert Coin:"))
    if coinInsert in coins:
        amountDue=amountDue - coinInsert
        insertTotal=insertTotal+coinInsert

print("Change Owed:", insertTotal-50 )

