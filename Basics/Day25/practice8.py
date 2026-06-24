# to find factor of any number
n=int(input("Enter number:"))
fac=[]
for i in range(1,n+1):
    if n%i==0:
        fac.append(i)
print(fac)        