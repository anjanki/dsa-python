arr=list(map(int,input().split()))
hash_map=dict()
for i in range(len(arr)):
 if arr[i] in hash_map:
  hash_map[arr[i]] +=1
 else:
  hash_map[arr[i]]=1
print(hash_map)   

           