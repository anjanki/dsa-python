#find the element of list d in strig s:
s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_map=dict()
for i in range(0,len(s)):
    if s[i] in hash_map:
        hash_map[s[i]] +=1
    else:
        hash_map[s[i]]=1
for j in range(0,len(q)) :
    if q[j] in hash_map:
        print(hash_map[q[j]]) 
    else:
        print(0)             
