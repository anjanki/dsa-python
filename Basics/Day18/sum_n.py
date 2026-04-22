#find sum of n natural number using recursion
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
num=int(input("Enter the number:"))
print (f"sum of 1st {num} number is {sum(num)}")