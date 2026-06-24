# #reverse array
# arr=list(map(int,input().split()))
# print(arr)
# #reversing array
# print(arr[: :-1])
#using second method
n=int(input("Enter the length of array:"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)   
revarr=[] 
for i in range(int(len(arr)-1),-1,-1):
    r=arr[i]
    revarr.append(r)
print(revarr)    