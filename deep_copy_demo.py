import copy 

list1 = [1,2,3,4]

list2 = list1
#shallow copy
print(id(list2))
print(id(list1))

list2.append(5) #any change in the refrence it can change into the main 
print(list1)
print(list2)

#deep copy
list3 = copy.deepcopy(list2)
list3.append(6) #no effect to the main 
print(list3)
print("-----Original List deep copy------")
print(list2)
