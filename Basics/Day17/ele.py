#function to print element of list
def ele_list(num):
    n=len(num)
    for i in range(0,n):
       print(num[i],end=" ")
    
list=[4,3,'anjan',22,'age']   
print(ele_list(list))   
