#tail recursion or backtracking
count=0
def fun():
    global count
    if count==4:
        return
    count+=1 
    fun()
    print("hello anjan")
    
fun()    
