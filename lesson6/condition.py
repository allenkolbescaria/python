h=float(input("enter your height in meters"))
w=float(input("enter your weight in kg"))
bmi=w/h**2
if bmi<25:
    print("you are under weight")
elif bmi<=35:
    print("you are healthy")
else:
    print("you are obese")