try:
  a= int(input("enter your age  :"))
  if a%2==0 :
    print("the age is even")
  else:
    print("the given age is odd")
except ValueError :
  print("an exception has occured")
