#virtual coin toss program
import random
def coin_toss():
    toss=random.randint(0,1)
    if toss==1:
        return "Head"
    else:
        return"tail"
    
result=coin_toss()
print("tossing coin....")
print("output:",result)
