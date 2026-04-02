# find minimum element of list using positive infinity
arr=list(map(int,input().split()))
min=float("inf")
for num in arr:
    if num<min:
        min=num
print(f"minimum element in array{min}")        