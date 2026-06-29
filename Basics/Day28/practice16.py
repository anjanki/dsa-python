#find the factor of any number using the half of the number 
n=int(input("Enter the value of n:"))
num=n
result=[]
for i in range(1,(n//2)+1):
    if num%i==0:
     
     result.append(i)
result.append(n)    
print(result)     
        

