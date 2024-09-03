loan_amount=200000

interest_rate=9

tenure=10

r=interest_rate/12/100

print(r)

n=tenure*12

one_plus_r=(1+r)**n

EMI=(loan_amount*r*one_plus_r)/(one_plus_r-1)

total_payable_amount=EMI*n

print(f"MOBTHLY EMI={EMI}")

print(f"total payable Amount={total_payable_amount}")

total_interest_payable=total_payable_amount-loan_amount

print(f"Toatal interest payable amount={total_interest_payable}")

