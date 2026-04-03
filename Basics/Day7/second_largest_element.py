#Find the second maximum value in the array such that:

#It is less than the maximum
#It is not equal to the maximum using second method
arr=list(map(int,input().split()))
largest=float('-inf')
second=float('-inf')
for num in arr:
    if num>largest:
      second=largest
      largest=num
    elif num>second and num !=largest:
      second=num
if second==float('-inf'):
   print(-1)
else:
   print(second)