#find the factor of given no.
num=int(input("Enter num:"))
arr=[]
#for i in range(1,num+1):
 #   if(num%i==0):
 #       arr.append(i)
#print(arr)  
#optimal method are:
# for i in range(1,(num//2)+1):
#     if(num%i==0):
#         arr.append(i)
# arr.append(num)
# print (arr)        
# more optimal:
from math import sqrt
for i in range(1,int(sqrt(num))+1):
    if(num%i==0):
     arr.append(i)
    if(num//i!=i):
     arr.append(num//i)
print(arr)       
