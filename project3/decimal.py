n=float(input("enter a decimal number"))
if n==float(int(n)):
    print("the binary representation is:  ",bin(int(n)).replace("0b",""))
else:
    print("the number is not decimal")