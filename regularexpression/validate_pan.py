from re import fullmatch

num=input("enter Pan Number ")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,num)

print("invalid" if matcher == None else "valid")