# frequncy map
n=list(map(int,input("Enter the element of array:").split()))
frequency_map=dict()
for i in range(0,(len(n))):
    if n[i] in frequency_map:
        frequency_map[n[i]]+=1
    else:
        frequency_map[n[i]]=1
print(frequency_map)        