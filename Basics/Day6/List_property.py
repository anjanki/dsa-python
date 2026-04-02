# different characterstic of list in python
num=[1,3,3,-3,5,24,14,21]
print(num)
print(max(num))
print(min(num))
print(len(num))
print(sum(num))
num.append(15)
print(num.pop())#when we know the index
print(num)
print(num.remove(21))#when we know value
print(num)
print(num.sort())
print(num)
num.sort(reverse=True)
print(num)
num.sort(reverse=False)
print(num)
print(num[1:-3])
num.append("anjan")
print(num)
num.insert(2,"Gaurav")#
print(num)
num.extend(["anjan",3,52,'a'])
print(num)
num[2:2]=[34,53]
print(num)
num[2:4]=[0,0]
print(num)


