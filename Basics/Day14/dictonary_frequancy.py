# find the frequency of dictionary 
nums=list(map(int,input().split()))
n=len(nums)
frequency_map={}
for i in range(n):
    if nums[i] in frequency_map:
        frequency_map[nums[i]]+=1
    else:
        frequency_map[nums[i]]=1
print(frequency_map)              

