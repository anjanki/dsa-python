# merge two shorted array:
num1=list(map(int,input().split()))
num1.sort()
num2=list(map(int,input().split()))
num2.sort()
result=[]
n,m=len(num1),len(num2)
i,j=0,0
while i<n and j<m:
    if num1[i]<=num2[j]:
      result.append(num1[i])
      i+=1
    else:
       result.append(num2[j])  
       j+=1
if i<n:
 while i<n:  
   result.append(num1[i])
   i+=1
else:  
   while j<m: 
    result.append(num2[i])
    j+=1
print(result)    

            
