expenses=[12000,13000,11000,14000,15000,21000,22000,13000]

expense_count=len(expenses)

print(len(expenses))

for i in range (0,expense_count):

    print(expenses[i])

for i in range(0,len(expenses)): 

    if expenses [i] >15000:

        print(expenses[i])

total_expenses=0

for i in range(0,len(expenses)):

    total_expenses=total_expenses+expenses[i]

print(f"Total expense={total_expenses}")

avg_expenese=total_expenses/len(expenses)

print(f"Average expense={avg_expenese}")




    


