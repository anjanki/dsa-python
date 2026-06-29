# # to check string is palindrome or not
# word=input("Enter the word:")
# if word==word[: :-1]:
#     print(word,"is palindrome")
# else:
#     print(word,"is not palindrom")    

s=(input("Enter the string:"))
r=s[::-1]
if(s==r):
    print(s,"palindrome")
else:
    print(s,"not palindrome")    