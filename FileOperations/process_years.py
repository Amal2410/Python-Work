f_read=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\FileOperations\\years.txt","r")
f_century=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\FileOperations\\century.txt","w")
f_non_century=open("C:\\Users\\Admin\\Desktop\\PythonJuneWorks\\FileOperations\\non_century.txt","w")

for year in f_read:

    y=int(year.rstrip("\n"))

    if y%100==0:

        f_century.write(str(y)+"\n")

    else:

        f_non_century.write(str(y)+"\n")



    