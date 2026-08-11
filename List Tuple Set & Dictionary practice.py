#List
list=["mango","banana","cherry","apple"]
print(list)

#length of the list
print(len(list))

#indexing
print(list[3])

#negative indexing
print(list[-1])

#change list item by refering the index 
number=[1,2,"mango",4,5]
number[2]= 3
print(number)

#add item
number.append(6)
print(number)

#insert item by telling where to insert using index
number.insert(2,"mango")
print (number)

#extend the list
num2=[7,8,9,10]
number.extend(num2)
print (number)