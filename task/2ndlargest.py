num1=int(input("Enter first number-"))

num2=int(input("Enter  second number-"))

num3=int(input("Enter third number-"))

if num2>num1>num3 or num3>num1>num2:

    print(f"the second largest number is {num1}")

elif num1>num2>num3 or num3>num2>num1:

    print(f"the second largest number is {num2}")

elif num2>num3>num1 or num1>num3>num2:

    print(f"the second largest number is {num3}")
