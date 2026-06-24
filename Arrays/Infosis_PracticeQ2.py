# You are given an integer `n`. A 0-indexed integer array `nums` of size `n + 1` is created using the following rules:

# 1. `nums[0] = 0`
# 2. `nums[1] = 1`
# 3. `nums[2 * i] = nums[i]` when `2 <= 2 * i <= n`
# 4. `nums[2 * i + 1] = nums[i] + nums[i + 1]` when `2 <= 2 * i + 1 <= n`

# Your task is to return the maximum value present in the array `nums`.
n=int(input())
nums=[0]*(n+1)
nums[0]=0
nums[1]=1
for i in range(1,(n//2)+1):
    nums[2*i]=nums[i]
    nums[2*i+1]= nums[i]+nums[i+1]
print(nums)    
print(max(nums))    

##second method
n = 7

nums = [0] * (n + 1)

if n >= 1:
    nums[1] = 1

for i in range(1, n + 1):

    if 2 * i <= n:
        nums[2 * i] = nums[i]

    if 2 * i + 1 <= n:
        nums[2 * i + 1] = nums[i] + nums[i + 1]

print(nums)
print(max(nums))