d = {}
n = int(input("Enter number of pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print(d)  