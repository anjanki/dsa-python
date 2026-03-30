#Day 3: Find leap_year
#patform:jenney lacture
#Discription: This program checks whether a given year is a leap year or not. 
#A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
#The program takes a year as input and displays the result accordingly
'''year=int(input("Enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year}is leap year")
        else:
            print(f"{year}is not leap year")    
    else:
        print(f"{year}is leap year")    
else:
    print(f"{year}is not leap year")'''

# in more optimal way
year=int(input("Enter year: "))
if (year%4==0 and year%100!=0) or(year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")    