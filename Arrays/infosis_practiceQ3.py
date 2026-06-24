arr=[7,8,5,5,9,2,2,0,1,6]
n=len(arr)
max_value=0

for start in range(n):
    #clock-wise
    res=[arr[(start+i)%n] for i in range(n)]
    ans=0
    total=0
    for i in res:
        ans^=i
        total+=ans
    max_value=max(max_value,total)  

    #anti-clockwise
    res=[arr[(start+i)%n] for i in range(n)]
    ans=0
    total=0
    for i in res:
        ans^=i
        total+=ans
    max_value=max(max_value,total)   
print(max_value)         


    