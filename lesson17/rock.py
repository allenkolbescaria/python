import random as r
list=["rock","paper","scissor"]
a=input("enter rock, paper or scissor   ")
b=r.choice(list)
print(f"the user choice is {a} and the computer choice is {b}")
if a==b:
  print("the match is a tie")
elif a=="paper":
  if b=="scissor":
    print("you have lost")
  else:
    print("you have won")
elif a=="scissor":
  if b=="rock":
    print("you have lost")
  else:
    print("you have won")
elif a=="rock":
  if b=="paper":
    print("you have lost")
  else:
    print("computer has chosen scissor and you have chosen rock you have won")
else:
  print("better luck next time")
  