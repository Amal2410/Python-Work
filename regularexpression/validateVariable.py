from re import fullmatch

variable_name=input("Enter Variable Name")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)

# if matcher==None:

#     print("invalid")

# else:

#     print("valid")

print("invalid" if matcher==None else "valid")