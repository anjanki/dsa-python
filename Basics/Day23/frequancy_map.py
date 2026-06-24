# frequancy map

# num=int(input("Enter the length of list:"))
# list=[]
# for i in range(0,num):
#     list.append(int(input()))
# print(list)  



#taking integer list in one line
# list1=list(map(int,input("Enter element:").split()))
# print(list1)

# taking list as string input
# list2=list(input("Enter string element:").split())
# print(list2)


#using list comprahession
# list=[int(x)for x in input().split()]
# print(list)

#frequancy map
# list=list(map(int,input().split()))
# print(list)
# frequncy_map=dict()
# for i in range(0,int(len(list))):
#     if list[i] in frequncy_map:
#         frequncy_map[list[i]] +=1

#     else:
#         frequncy_map[list[i]]=1
# print(frequncy_map)  


# second method to print  
list=list(map(int,input().split()))
hash_map=dict()
for i in range(0,int(len(list))):
    hash_map[list[i]]=hash_map.get(list[i],0)+1

print(hash_map)







