# fabonacci  0 1 1 2 3 5 ...
n=int(input("Enter the number : "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    # tem=a
    # a=b
    # b=tem+b
    a,b=b,a+b

    
