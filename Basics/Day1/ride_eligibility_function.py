# day 1:Nested if else example using function
#program : check eligibility of ride and amout condition based on age and height.
def ride_eligibility(age,height):
    if height>=3:
        print("you can ride")
        if age<18:
            return"pay INR :250💰"
        else:
            return"Pay INR :500💰"
    else:
     return("You can't take ride")
#input
height=int(input("Enter height in feet:"))
age=int(input("Enter the age:"))
result=ride_eligibility(age,height)
print(result)
print("\nThank you for visting! Have a nice 😊")

