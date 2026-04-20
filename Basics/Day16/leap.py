# to check leap year:
num=int(input("Enter Year:"))
if num%4==0:
 if num%100==0:
   if num%400==0:
     print(f"leap year") 
   else:
     print(f"Not leap year")  
 else:
   print(f"Not a leap year")
else: 
 print(f"Not a leap year")
