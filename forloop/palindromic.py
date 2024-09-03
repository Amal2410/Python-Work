num=int(input("Enter the number="))

result=0

number=num

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

print(result)

if number==result:

    print(f"Number is palindrom")

else:

    print(f"Number is not palindrom")

   
