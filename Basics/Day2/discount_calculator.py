# Day 2 :Discount calculator 
#platform:Tcs /practice problem
#Discription: Apply discount based on amount and print final payable amount.
'''amt=int(input("Enter you amount  in INR :"))
if amt<1000:
    f_amt=amt-(amt*0.05)
    print(f"pay INR :{f_amt:.2f}")
elif amt>1000 and amt<5000:
    f_amt=amt-(amt*0.1)
    print(f"pay INR :{f_amt:.2f}")
elif amt>=5000:
    f_amt=amt-(amt*0.15)
    print(f"pay INR :{f_amt:.2f}")'''
# efficiant way
'''amount=int(input())
if amount<1000:
    final_amt=amount-(amount*0.05)
elif amount>=1000 and amount<5000:
    final_amt=amount-(amount*0.1)
else:
    final_amt=amount-(amount*0.15)

print(f"{final_amt:.2f}")   '''
# more efficiant
amt=int(input())
if amt<1000:
    discount=0.05
elif amt>=1000 and amt<5000:
    discount=0.1
else:
    discount=0.15
final_amt=amt-(amt*discount)
print(f"{final_amt:.2f}")



