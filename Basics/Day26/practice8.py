#print 1 to n using tail recursion or backtraking 
def fun(i,n):
    if i>n:
     return
    fun(i+1,n)
    print(i)
fun(1,10)    
# it print n to 1 
