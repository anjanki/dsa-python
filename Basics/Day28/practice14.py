#reverse the string
s=input("Enter the string:")
word=s
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)

if rev==word:
    print(word,"is palindrome")
else:
    print(word,"is not palindrome")    



