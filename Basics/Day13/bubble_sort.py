# bubble sort
n=int(input())
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)            
