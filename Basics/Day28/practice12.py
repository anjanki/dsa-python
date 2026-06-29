# count the number using log10 functon
n=int(input("Enter the num:"))
from math import log10
def countdigit(n):
    return int(log10(n))+1
print(countdigit(n))
