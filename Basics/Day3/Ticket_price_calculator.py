# Day X: Multiple If-Else (Ticket Price Calculator)
# Platform: Jenny Lecture
# Description:
# This program determines whether a person can ride based on height.
# If eligible, it calculates the ticket price based on age:
# - Age < 12 → Rs. 150
# - Age 12 to 18 → Rs. 250
# - Age > 18 → Rs. 500
# Additionally, the user can choose to take a photo,
# which adds Rs. 50 to the total bill.
height=int(input("What is your height in feet ? :"))
if height>=3:
    bill=0
    Age=int(input("what is your age ?"))
    if Age<12:
        bill=150
        print("Ticket Price INR: 150")
    elif Age<=18:
        bill=250
        print("Ticket Price INR:250")
    else: 
        bill=500
        print("Ticket Price INR:500")
    want_photo=input("Do you want to take photo (Y/N)?") 
    if want_photo=='Y' or want_photo=='y':
        bill+=50
    print(f"your total bill is INR:{bill}")
else:
    print("You can't ride")    
