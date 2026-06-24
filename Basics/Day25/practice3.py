#count of digit using log function
num=int(input("Enter the n:"))

from math import*
def countdigit(num):
    return int(log10(num))+1

print(countdigit(num))