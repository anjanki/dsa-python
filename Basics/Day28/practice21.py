#find d element in s for string
s="azyxyyzaaaa"
d=["d","a","y","x"]
for ch in d:
   count=0
   for x in s:
      if ch==x:
         count +=1
   print(ch,"->",count)     
      

