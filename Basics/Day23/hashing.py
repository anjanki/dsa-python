list1=[5,3,2,2,1,5,5,7,5,10]
list2=[10,111,1,9,5,67,2]
for num in list2:
    count=0
    for x in list1:
        if x==num:
            count +=1
    print(count)    