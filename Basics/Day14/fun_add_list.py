# merge two shorted list

def merge_list(num1,num2):
    n,m=len(num1),len(num2)
    i,j=0,0
    result=[]
    while i<n and j<m:
        if num1[i]<=num2[j]:
            result.append(num1[i])
            i+=1
        else:
            result.append(num2[j])
            j+=1
    if i<n:
     while i<n:
        result.append(num1[i]) 
        i+=1
    else:
       while j<m:
          result.append(num2[j])
          j+=1   
    return result 
#input 
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
result=merge_list(num1,num2)
print(result)
