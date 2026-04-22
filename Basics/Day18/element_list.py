#print all element of list.
num=list(map(int,input("Enter element of list:").split()))
# n=len(num)
# for i in range(0,n):
#     print(num[i] ,end=" " )
print(*num, sep="\n") # for short cut using unpacking


