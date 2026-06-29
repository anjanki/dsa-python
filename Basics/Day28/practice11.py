#count of digit
n=int(input("enter the value of n:"))
num=n
count=0
while num>0:
    num//=10
    count +=1
print(count)    