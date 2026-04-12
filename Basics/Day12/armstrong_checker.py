# to check given number is armstrong or not

n = int(input())
original = n   # store original number

# count digits
c = 0
temp = n
while temp > 0:
    temp //= 10
    c += 1

# calculate armstrong sum
total = 0
temp = n
while temp > 0:
    last_digit = temp % 10
    total += last_digit ** c   # correct formula
    temp //= 10

# check result
if original == total:
    print(f"{original} is an armstrong")
else:
    print(f"{original} is not armstrong")