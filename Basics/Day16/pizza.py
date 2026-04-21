Size=input("Enter the size of pizza(S/M/L)?")
Bill=0
if Size.lower()=='s':
  Bill+=100
  print(f"{Bill} is your bill")
elif Size.lower()=='m':
  Bill+=200
  print(f"{Bill} is your bill")
elif Size.lower()=='l':
  Bill+=300
  print(f"{Bill} is your bill") 
else:
  print("invalid input") 
P=input("Do you want pepporoni(Y/N)")
if P.lower()=='y' and Size=='l' or Size=='m' :
  Bill+=50
elif P.lower()=='y'and Size=='s':
  Bill+=30
else:
  Bill+=0  
Ch=input("Do you want extra cheese (Y/N)")
if Ch.lower()=='y':
  Bill+=20
print(f"{Bill} is your bill")          
    
