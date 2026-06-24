# to check armstrong or not
n=int(input("Enter num:"))
num=n
#counting digit
count=0
while num>0:
    num//=10
    count +=1
print("number of digit",count) 
num=n #reset num
result=0 
#extraction of digit
while num>0:
 ld=num%10 
 result +=(ld**count)
 num //=10
print(result) 
#to check armstrong
if result==n:
   print(n,"is armstrong")
else:
   print(n,"is not armstrong")   

