#reverse string
s=input("Enter string:")
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)   
if s==rev:
    print("it is palindome")
else:
    print("it is not palindrome")


   
    