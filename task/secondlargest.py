num1=int(input("Enter first number-"))

num2=int(input("Enter  second number-"))

num3=int(input("Enter third number-"))

if num1>num2 and num1>num3:

    if num2>num3:

        print(f"the second largest number is {num2}")

    else:
        
        print(f"the second largest number is {num3}")

if num2>num1 and num2>num3:

    if num1>num3:

        print(f"the second largest number is {num1}")

    else:
        
        print(f"the second largest number is {num3}")

if num3>num1 and num3>num2:

    if num1>num2:

        print(f"the second largest number is {num1}")

    else:
        
        print(f"the second largest number is {num2}")