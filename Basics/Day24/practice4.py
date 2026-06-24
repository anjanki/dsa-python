#check the plindorme
n=int(input("Enter the number:"))
num=n
while num>0:
    digit=num%10
    ld=digit*10+digit
    print(digit,end="")
    num//=10

