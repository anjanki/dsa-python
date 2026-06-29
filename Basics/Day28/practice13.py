#find palindrome or not 
n=int(input("Enter the number"))
num=n
rev=0
while num>0:
    ld=num%10
    rev=(rev*10)+ld
    num//=10

if n==rev:
    print(n,"is palindrome") 
else:
    print(n,"is not palindorme")       


