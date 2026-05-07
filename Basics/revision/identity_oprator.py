# intentity oprator is and not is and ==
a=3
b=3
c='3'
print(a==b)
print(a is b)
print(a is not b)
print(a is c)
print(id(a))
print(id(b))
print(id(c))
a=3
print(a is a)
print(id(a))
print(a==a)
b=3.0
print(a is b)#due to different class float and integer
print(id(a))
print(id(b))
