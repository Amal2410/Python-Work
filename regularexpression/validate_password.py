from re import fullmatch

password=input("Enter Password ")

pattern="[A-Z][1-9][0-9][0\\s][0-9]{4}[1-9]"

matcher=fullmatch(pattern,password)

print("invalid" if matcher == None else "valid")