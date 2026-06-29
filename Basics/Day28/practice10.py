# extraction of digit
n=int(input("Enter the number:"))
num=n
while num>0:
    print(num%10)
    num//=10
    