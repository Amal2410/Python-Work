# from re import finditer

# text="hellopythonhellopythonhellopython"

# matcher=finditer("python",text)

# count=0

# for m in matcher:

#     print(m.start(),"===",m.group())

#     count+=1

# print("total count",count)

# from re import finditer

# text="abc123 @k#7LMdef"

# pattern="[abf]"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"===",m.group())

# from re import finditer

# text="abc123 @k,#7LMdef"

# pattern="[a-zA-Z]"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"===",m.group())

# from re import finditer

# text="abc123 @k,#7LMdef"

# pattern="[^0-9]"

# matcher=finditer(pattern,text)

# for m in matcher:

#     print(m.start(),"==",m.group())

from re import finditer

text="abc123 @k,#7LMdef"

pattern="[a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())
