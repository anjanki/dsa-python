#another method to find factor of number
n=int(input("Enter number:"))
result=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        result.append(i)
result.append(n)
print(result)