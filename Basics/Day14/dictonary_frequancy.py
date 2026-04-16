# find the frequency of dictionary 
nums=list(map(int,input().split()))
n=len(nums)
frequency_map={}
for i in range(n):
    if nums[i] in frequency_map:
        frequency_map[nums[i]]+=1
    else:
        frequency_map[nums[i]]=1
max_key=max(frequency_map,key=frequency_map.get) #to max key and value both
print(max_key,frequency_map[max_key])       
print(max(frequency_map.values())) # to find only max value of key             

