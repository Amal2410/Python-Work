weight=int(input("Enter the weight-"))

height=int(input("Enter the height-"))

height_in_m= height / 100

bmi_result= weight/height_in_m**2

print(f"Bmi={bmi_result}")

if bmi_result<19:

    print("Under weight")

elif bmi_result>=19 and bmi_result<25:

    print("Normal")

elif bmi_result>=25 and bmi_result<30:

    print("Over weight")

elif bmi_result>30:

    print("Obisity")




