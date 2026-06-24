#count the digit:
n=int(input("Enter the number:"))
num=n
count=0
while num>0:
    num //=10
    count +=1
print(count)   
 