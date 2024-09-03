from re import fullmatch

f=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\regularexpression\\domain.txt")

pattern="[\w\W]+\\.com"

for line in f:

    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher !=None:

        print(domain)
