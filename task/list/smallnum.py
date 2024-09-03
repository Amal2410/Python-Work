num=[1,3,2,5,7,9,10,4]

num.sort()

print(num[0])

num=[1,3,2,5,7,9,10,4]

smallest_num=num[0]

for i in num:

    if i<smallest_num:

        smallest_num_num=i

print(f"Smallest number is {smallest_num}")