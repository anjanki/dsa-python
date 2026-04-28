n=int(input("Enter the number: "))
num=n
rev=0
while num>0:
   last_digit=num%10
   rev=rev*10+last_digit
   num //=10
if n==rev:
   print("palindrome") 
else:
   print("not palindrome")  
   
   
    