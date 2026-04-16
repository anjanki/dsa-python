# find max value of key in dictonary
nums=list(map(int,input().split()))
n=len(nums)
frq_map=dict()
for i in range(n):
    if nums[i] in frq_map:
        frq_map[nums[i]]+=1
    else:
        frq_map[nums[i]]=1
print(frq_map)        
# print(max(frq_map.values()))            