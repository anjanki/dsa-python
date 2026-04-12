# short cut to check the palindrome of number using sclicing 
n=input()
s=n[: :-1]
if s==n:
    print(f"{n}:is palindrome")
else:
    print("not palindrome")

