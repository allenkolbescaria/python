a=int(input("enter the actual value"))
s=int(input("enter the selling price"))
if s>a:
    print(f"the business is having profit of{s-a} ")
else:
    print(f" the business is facing loss of rupees {a-s}")