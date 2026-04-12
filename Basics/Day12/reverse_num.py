#To reverse number ex input:123, output:321
n=int(input())
rev=0
while n>0:
    last_digit=n%10
    rev=rev*10+last_digit
    n//=10 # remove last digit
print(rev)

    

