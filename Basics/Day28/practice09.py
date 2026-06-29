# print 1 to n using tail recursion/ backtracking
def fun(i,n):
    if i>n:
        return
    fun(i+1,n)
    print(i)
fun(1,15)    