try:
  num1,num2=eval(input("enter the numbers  "))
  result=num1/num2
  print("the division is  ",result)
except ZeroDivisionError as e:
  print("there is a zero division error ",e)
except ValueError as e:
  print("there is a  value error ",e)
except SyntaxError as e:
  print("there is a zero division error ",e)
except:
  print("there is an exeption in general")
finally:
  print("no error can stop the code")
