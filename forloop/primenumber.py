num=int(input("enter the number="))

isPrime=True

for i in range (2,num):

    if num%i==0:

        isPrime=False

        break

print(f"{num} is prime" if isPrime==True else f"{num} not prime")