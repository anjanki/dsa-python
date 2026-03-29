#Day 2: parking fine calculator
#platform:Tcs /practice problem 
#discriptiion : calculte fine based on parking hour
hour=int(input())
if hour<=2:
    print(f"{100}")
elif hour>2 and hour<=5:
    print(f"{50}")
else:
    print(f"{20}")