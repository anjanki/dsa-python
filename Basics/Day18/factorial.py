def factorial(num):
 fac=1
 for i in range(num,0,-1):
   fac=fac*i
 print(fac)   
n=int(input("Enter the number:"))
factorial(n)

