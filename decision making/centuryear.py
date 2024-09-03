year=int(input("Enter year-"))

if year%100==0:

    print(f"{year} is century year")

elif year%100!=0:

    print(f"{year} is not century year")