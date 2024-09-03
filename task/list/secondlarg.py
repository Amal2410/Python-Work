num=[1,3,2,5,7,9,10,4]

num.sort()

print(num[-2])

num=[1,3,2,5,7,9,10,4]

largest_num=num[0]

second_largest=num[0]

for i in num:

    if i>largest_num and i>second_largest:

        second_largest=largest_num

        largest_num=i

print(f"Second largest number is {second_largest}")