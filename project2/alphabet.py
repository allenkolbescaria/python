n=input("enter the character")
if len(n)==1:
    if ('a'<=n<='z')or('A'<=n<='Z'):
        print("the given character is an alphabet")
    else:
        print("the given character is not a n alphabet")
else:
    print("enter only one character")
