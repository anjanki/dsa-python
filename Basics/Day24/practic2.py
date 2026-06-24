#extraction of digit
num=int(input("Enter the number:"))
num2=num
while num2>0:
    x=num2%10
    print(x,end=" ")
    num2=num2//10
