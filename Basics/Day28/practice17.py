#print factor of any number using sqrt method
n=int(input("Enter the value of n:"))
num=n
result=[]
from math import sqrt
for i in range (1,int(sqrt(num))):
    if num%i==0:
        result.append(i)
    if num//i !=i:
        result.append(num//i)  
print(result)          
    