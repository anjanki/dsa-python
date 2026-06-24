# num1=int(input())
# for i in range(1,num1+1):
#     if num1%i==0:
#       print(i,end=" ")

#using list
# num2=int(input())
# result=[]
# for i in range(1,num2+1):
#    if num2 % i==0:
#       result.append(i)
# print(result)      

#reduce  find the factor using n//2 and in last add the end value
# num3=int(input())
# result=[]
# for i in range(1,num3//2):
#     if num3%i==0:
#         result.append(i)
# result.append(num3)
# print (result)        

#find more optimal solution:
from math import sqrt
num4=int(input())
result=[]
for i in range(1,int(sqrt(num4))+1):
    if num4 %i==0:
      result.append(i)
    elif num4 //i !=i:
       result.append(num4//i) 
result.sort()       
print(result);      





