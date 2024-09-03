arr=[
    [12,23],
    [20,35],
    [40,50]
]

numbers=[]

for lst in arr:

    for num in lst:

        numbers.append(num)

print(sum(numbers))

evens=[num for lst in arr for num in lst if num%2==0]

print(evens)