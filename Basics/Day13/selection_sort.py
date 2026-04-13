#arr=list(map(int,input().split()))
#print(arr)

n=int(input())
list=[]
for i in range(n):
  x=int(input()) 
  list.append(x) 
print(list)   
# selection sort
size=len(list)
for i in range(0,size):
    min_index=i
    for j in range(i+1,size):
      if list[j]<list[min_index]:
        min_index=j
    list[i],list[min_index]=list[min_index],list[i]
    
print(list)        
        
 
