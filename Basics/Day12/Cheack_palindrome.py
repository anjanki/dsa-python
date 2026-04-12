# To Cheack palindrome of number
n=int(input())
orginal_num=n
rev=0
while n>0:
    l_digit=n%10
    rev =rev*10+l_digit
    n //=10 #remove last digit
if rev==orginal_num:
    print(f"{orginal_num}: is palindrome")
else:
    print(f"{orginal_num}:is not palindrome")
