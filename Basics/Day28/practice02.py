#check no is armstrong
n=int(input("Enter the value of num:"))
num=n
count=0
result=0
while num>0:
     num//=10
     count +=1
num=n
while num>0:
      ld=num%10
      result+=(ld**count)
      num//=10

if n==result:
      print(n,"is armstrong") 
else:
      print(n,"not armstrong")           
    
