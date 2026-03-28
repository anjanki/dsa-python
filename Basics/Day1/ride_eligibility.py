# Day 1: Nested if-else example
# Program: Check if a person can ride based on height and age
height=int(input("Enter height in feet:"))
if height>=3:
     print("you can take ride")
     age=int(input("Enter your age:"))
     if age<18:
        print("pay INR:250")
     else:
        print("Pay INR:500")
else:
    print("you can't ride") 
print("\nThank you for visiting! Have a nice day 😊")      
