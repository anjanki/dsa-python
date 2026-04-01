# who will pay bill? using  random bultin function
import random
name=input("Enter the Name seprated by comma:")
name_list=name.split(",")
print(name_list)
size=len(name_list)
selector=random.randint(0,size-1)
print(f"{name_list[selector]} will pay the bill")
