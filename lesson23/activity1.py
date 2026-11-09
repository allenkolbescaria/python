my_set={1,2,3}
print(my_set)
my_set={1.0,"hello ",(1,2,3)}
print(my_set)
my_set={1,2,3,2,1}
print(my_set)
my_set=set([1,2,3,2])
print(my_set,"/n")
num_set=set([0,1,2,3,4,5])
print("original set:")
print(num_set)
num_set.pop(3)
print("after removing the first element of the set")
print(num_set)