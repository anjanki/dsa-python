weight=float(input("Enter weight in kg:"))
height=float(input("Enter the height in m:"))
Bmi=(weight*weight)/(height*height)
if Bmi<18.5:
    print("Under weight")
elif 18.5>=Bmi<=29.9:
    print("Normal weight")
else:
    print("obese")