#checking num is palindrome or not
n=int(input("Enter the number:"))
num=n
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num //=10
print(rev) 
palindrome=True
not_palindrome=False
if n==rev:
    print(palindrome) 
else:
    print(not_palindrome)    
