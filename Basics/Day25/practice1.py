#extraction of digit:
n=int(input("Enter the number:"))
num=n
while num>0:
    x=num%10
    print(x,end="")
    num=num//10
