#print 1 to n using recursion it means head recursion
def fun(i=1,n=10):
    if i>n:
        return
    print(i)
    
    fun(i+1,n)

fun()    
