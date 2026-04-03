#Find the second maximum value in the array such that:

#It is less than the maximum
#It is not equal to the maximum
arr=list(map(int,input().split())) #input list from users
arr=list(set(arr))
arr.sort()
if len(arr)<2:
    print(-1)
else:
    print(arr[-2])