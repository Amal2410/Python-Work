num=[1,2,3,4,5,6,7]

lastdigit=(num.pop(-1))

firstdigit=(num[0])

num[0]=lastdigit

num[-1]=firstdigit

print(num)