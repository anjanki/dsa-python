# #another method to find factor of number
# n=int(input("Enter number:"))
# result=[]
# for i in range(1,(n//2)+1):
#     if n%i==0:
#         result.append(i)
# result.append(n)
# print(result)

n=int(input("Enter the num:"))
fac=[]
for i in range(1,(n//2)+1):
    if (n//2)%i==0:
        fac.append(i)
fac.append(n) 
print(fac)   


