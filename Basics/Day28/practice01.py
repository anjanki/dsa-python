#find frequency using hash map
arr=list(map(int,input("Enter the element of array:").split()))
hash_map=dict()
for num in arr:
    if num in hash_map:
        hash_map[num]+=1
    else:
        hash_map[num]=1
print(hash_map)            
