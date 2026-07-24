

a=int(input("enter the amount to be withdrawn"))
print("number of 100 rupee we need ", a//100)
a=a%100
print("number of 50 rupee notes we need", a//50)
a=a%50
print("number of 10 rupee notes we need", a//10)
a=a%10
print("number of 1 rupee coins we need", a//1)

