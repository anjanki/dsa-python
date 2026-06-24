#You are given:

# a string representing a positive number
# a digit character

# Your task is to remove exactly one occurrence of the given digit from the number so that the resulting number becomes as large as possible.

# It is guaranteed that the digit appears at least one time in the number.
n=input()#1321
d=input()#1
ans=[]
for i in range(len(n)):
    if n[i]==d:
        t=n[0:i]+n[i+1:]# before i and after i  but not included i
        ans.append(t)
print(max(ans))    
