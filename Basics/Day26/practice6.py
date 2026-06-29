#recursion using parameter
def fun(num,n):
    if n==0:
        return
    print(num)
    fun(num,n-1)
fun(15,4)    