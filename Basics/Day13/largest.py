# find largest element in array
n=int(input())
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)    
# find largest number
largest=arr[0]
for i in range(0,n):
    if largest<arr[i]:
        largest=arr[i]
print(largest)        
        