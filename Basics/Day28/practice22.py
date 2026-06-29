#find "d" in s using hash map
s="azyxyyzaaaa"
d=["d","a","y","x"]
hash_map=dict()
for ch in s:
    if ch in hash_map:
        hash_map[ch] +=1
    else:
        hash_map[ch]=1
for ch in d:
    if ch in hash_map:
        print(ch,"->",hash_map[ch])
    else:
        print(ch,"->",0)                