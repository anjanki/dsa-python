#print 1 to n using head recursion
def fun(n):
  if n==0:
    return
  print(n)
  fun(n-1)

fun(13)  