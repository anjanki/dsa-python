name1=input("Enter your name:")
name2=input("Enter your love:")
n1,n2=name1.lower(),name2.lower()
#count n1 and nu for 't','r','u','e'
t=n1.count('t')
r=n1.count('r')
u=n1.count('u')
e=n1.count('e')
t=n2.count('t')
r=n2.count('r')
u=n2.count('u')
e=n2.count('e')
total1=t+r+u+e
print(total1)
#count for love
l=n1.count('l')
o=n1.count('o')
v=n1.count('v')
e=n1.count('e')
l=n2.count('l')
o=n2.count('o')
v=n2.count('v')
e=n2.count('e')
total2=l+o+v+e
result=(total1*10)+total2
if result<=40:
    print(F"your love score is {result}%")
elif result>40<=90:
    print(F"{result}% is good patner")
else:
    print(f"{result}% made for each other")    



