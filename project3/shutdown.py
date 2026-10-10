def shutdown():
  if a=="yes"or a=="YES":
    print("All the systems are off shutdown")
  else:
    print("The conditions are not satisfied shut down overruled")

a=input("Are all the systems off or not  :",)
print(shutdown())