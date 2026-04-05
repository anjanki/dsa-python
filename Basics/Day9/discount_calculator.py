#discount calculator 
amt=int(input())
if amt<1000:
    d=0.05
elif amt>=1000 and amt<5000:
    d=0.1
else:
    d=0.15    
print(f"{(amt-amt*d):.2f}")