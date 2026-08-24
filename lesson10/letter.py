n=input("enter a word")
char=input("enter a single character")
i=0
count=0
while i<len(n):
    if n[i]==char:
        count=count+1
    i=i+1
print(count)