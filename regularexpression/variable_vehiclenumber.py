from re import fullmatch

vehicle_num=input("Enter Vehicle Number : ")

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")