#to find factor of any number:
n=int(input("enter number:"))
fac=[]
num=n
for i in range(1,n+1):
   if num%i==0:
    fac.append(i)
print(fac)    