# print fabonacci using recursion 
def fab(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
        
num=int(input("Enter the number: "))
for i in range(num):
 print(fab(i))