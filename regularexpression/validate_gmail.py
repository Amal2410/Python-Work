from re import fullmatch

gmail_id=input("enter Gmail id ")

pattern="\\w[\\w\\._]*+@gmail.com"

matcher=fullmatch(pattern,gmail_id)

print("invalid" if matcher == None else "valid")