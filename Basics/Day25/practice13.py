# #find frequency using hash map
# arr=list(map(int,input().split()))
# n=len(arr)
# hash_map={}
# for i in range(0,n):
#     hash_map[arr[i]]=hash_map.get(arr[i],0)+1
# print(hash_map)    

### repeat for practice:
arr=list(map(int,input().split()))
hash_map={}
for i in range(0,len(arr)):
    hash_map[arr[i]]=hash_map.get(arr[i],0)+1
print(hash_map)    