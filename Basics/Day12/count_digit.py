#  To count digit 
n=int(input())
digit_count=0
while n>0:
    last=n%10
    digit_count+=1
    n//=10#remove_last_digit
print(digit_count)
