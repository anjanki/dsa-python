# find the frequency of number in list or arry
arr=list(map(int,input().split()))
dictorny_map=dict()
for i in range(0,len(arr)):
    if arr[i] in dictorny_map:
        dictorny_map[arr[i]]+=1
    else:
        dictorny_map[arr[i]]=1
print(dictorny_map)        