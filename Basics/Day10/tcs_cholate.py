'''PROBLEM STATEMENT:A chocolate factory is packing chocolates into 
the packets. The chocolate packets here represent an array  of 
N number of integer values. The task is to find the empty
packets(0) of chocolate and push it to the end of the
conveyor belt(array).'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
result=[]
for j in range(n):
    if arr[j]!=0:
     result.append(arr[j]) 
result.sort()     
zero_count=n-len(result)
for i in range(zero_count):
   result.append(0)
print(result)

