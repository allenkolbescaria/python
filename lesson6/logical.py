
a=24
b=25
c=30
if a and b and c:
    print("all th values are integer")
else:
    print("all the values are not integer")


# - This becomes True only if all three values are treated as True.


# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a=10
b=-10
c=0
if a>0 or b>0:
    print("the values are greater than 0")
else:
    print("the values are less than 0")
    
if b>0 or c>0:
    print("either b or c is greater than 0")
else:
    print("both numbers are less than 0")



# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

