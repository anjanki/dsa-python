#check no is armstrong or not
n=int(input("enter the number :"))
num=n
l=len(str(num))
result=0
while num>0:
    ld=num%10
    result+=(ld**l)
    num//=10
if n==result:
    print(n,"is armstrong")  
else:
    print(n,"is not armstrong")  




 
   




   
   
       


