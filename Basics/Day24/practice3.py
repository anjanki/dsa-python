# #count digit
# n=int(input('Enter n:'))
# num=n
# count=0
# while num>0:
#      num//=10
#      count +=1
# print(count)  
#using second method:
num=int(input("Enter the num:"))
from math import *
def countdigit(num):
    return int(log10(num)+1)
print(countdigit(num))