s1=[1,2,3]
s2=['a','b','c']
s3=list(zip(s1,s2))
print(s3)
list1=[10,20,30,40,50]
list2=[100,200,300,400,500]
for x,y in zip(list1,list2[::-1]):
    print(x,y)
stocks=["reliance","infoys","tcs"]
prices=[2127,2432,7253]
new_dict={x:y for x,y in zip(stocks,prices)}
print(new_dict)
