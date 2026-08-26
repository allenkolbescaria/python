r=int(input("enter the rows"))
count=1
for i in range(0,r):
    for j in range(0,i+1):
        print(count,end=' ')
        count=count+1
    print()