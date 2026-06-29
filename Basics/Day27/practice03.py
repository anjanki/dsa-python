#find frequency of m element in n
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_map=dict()
for i in range(0,len(n)):
    if n[i] in hash_map:
        hash_map[n[i]]+=1
    else:
        hash_map[n[i]]=1
for j in range(0,len(m)):    
    if m[j] in hash_map:
        print(m[j],"->",hash_map[m[j]])
    else:
     print(m[j],"->",0) 
      


    