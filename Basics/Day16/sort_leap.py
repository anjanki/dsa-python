#to check leap year using and ,or
n=int(input("Enter the year"))
if n%400==0 or (n%100==0 and n%4==0):
    print(f"{n} is leap year")
else:
    print("not leap year")    