# 🍕 Pizza Order Program

# Take pizza size input
size = input("What size pizza do you want (S/M/L)? ").upper()

bill = 0

# Calculate base price
if size == 'S':
    bill += 100
    print("Small Pizza price is 100 Rs.")
elif size == 'M':
    bill += 200
    print("Medium Pizza price is 200 Rs.")
elif size == 'L':
    bill += 300
    print("Large Pizza price is 300 Rs.")
else:
    print("Invalid size selected!")
    exit()

# Ask for pepperoni
add_pepperoni = input("Do you want pepperoni (Y/N)? ").upper()

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 30
        print("Pepperoni added for 30 Rs.")
    else:
        bill += 50
        print("Pepperoni added for 50 Rs.")

# Ask for extra cheese
add_cheese = input("Do you want extra cheese (Y/N)? ").upper()

if add_cheese == 'Y':
    bill += 20
    print("Extra cheese added for 20 Rs.")

# Final bill
print(f"Your total bill is: {bill} Rs.")