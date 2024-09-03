f=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\FileOperations\\landslide.txt","r")

data=[]

for line in f:

    lst=line.rstrip("/n").split(" ")

    dic={"State":lst[0],"year":lst[1],"Deaths":int(lst[2])}

    data.append(dic)

print(data)

death_per_state={}

for dic in data:

    state=dic.get("State")

    death_count=dic.get("death_count")

    if state in death_per_state:

        death_per_state[state]+=death_count

    else:

        death_per_state[state]=death_count

print(death_per_state)    



