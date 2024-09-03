num=[1,3,2,5,7,9,10,4]

num.sort()

print(num[-1])

num=[1,3,2,5,7,9,10,4]

largest_num=num[0]

for i in num:

    if i>largest_num:

        largest_num=i

print(f"Largest number is {largest_num}")