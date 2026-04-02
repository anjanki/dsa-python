arr=list(map(int,input().split()))
#to print max element of arr usning sentinel value
largest=float("-inf")
for num in arr:
    if num>largest:
        largest=num
print(f"Largest element in array:{largest}")        

          