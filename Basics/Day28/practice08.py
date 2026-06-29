#print 1 to n using recursion:
def fun(i,n):
    print(i)
    if i>=n:
        return
    fun(i+1,n)
fun(1,40)    