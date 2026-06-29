#tail recursion
count=0
def fun():
 global count
 if count==4:
  return
 count+=1
 print("Hi, Anjan")
 fun()

fun() 
    