from re import finditer

text="abc 7Klefg@u"

# pattern="\d"

# pattern="\D"

# pattern="\w"

# pattern="\\W"

pattern="\S"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())

