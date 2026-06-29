#head recursion:
count=0
def fun():
    global count
    if count==4:
        return
    print("anjan")
    count +=1
    fun()

fun()    