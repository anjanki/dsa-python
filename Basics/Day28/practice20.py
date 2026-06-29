#third method to find element of m in n using hash map concept:
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_map=[0]*11
for num in n:
    hash_map[num] +=1
for num in m:
    if num<1 or num>10:
        print(num,"->",0)    
    else:
        print(num,"->",hash_map[num])


