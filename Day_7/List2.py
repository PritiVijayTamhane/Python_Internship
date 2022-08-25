
#List using constructor
from ast import Del


fruitList = list(("grapes", "banana", "apple"))
print(fruitList)  

fruitListwithoutsingonstructor = ["grapes", "banana", "apple"]
print(fruitListwithoutsingonstructor)
print(type(fruitListwithoutsingonstructor ))

remixlist = list(("grapes", "21.5", "Name", "@", "grapes"))
print(remixlist)
print(type(remixlist))

#Changing the elements

fruitList[0] = "Mango"
print(fruitList) 

newfruitList = ["apple", "cherry", "orange", "kiwi", "mango"] 
print(newfruitList)

newfruitList[1 : 3] = ["banana", "grapes", "strawberry"]
print(newfruitList)

newfruitList = ["orange", "kiwi", "mango"] 
print(newfruitList)
newfruitList[1 : 3] = ["apple"]
print(newfruitList)

#Using insert() method
newfruitList.insert(2, "Banana")
print(newfruitList)

#Using append() method to insert element at the end of the list
newfruitList.append("kiwi")
print(newfruitList)

#Using extend() method 
extendedlist = newfruitList.extend(fruitList)
print(extendedlist)

list1 = ["orange", "kiwi", "mango"] 
list2 = ["grapes", "banana", "apple"]

list1.extend(list2)
print(list1)

tuple = ("grapes", "banana", "apple")

list1.extend(tuple)
print(list1)

#Using remove method

list1.remove("grapes") 
print(list1)

list1[1 : 3] = []
print(list1)
 
list1.pop(2)
print(list1)

#Using 'del' keyword
del list1[0]
print(list1)

del list1[1]
print(list1)

del list1[0 : 3]
print(list1)

fruitList = ["grapes", "banana", "apples"] 
print(fruitList)
print(len(fruitList))

numList= [1, 5, 10, 9, 3]
booleanList = [True, False, False]
mixDatatypeList= ["shiv", 25, True, 50000000, "male"]

print(numList)
print(booleanList)
print(mixDatatypeList)

