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

#tuple
"tuples are immutable we cannot change it, once its created."
" So if we want to delete or  add an item we convert the tuple into list"
" do the rest of changes we need then we  converted that list into tuple again."
tuple_a = (1, 2, 3, 4, 5)
print(tuple_a) 

new = list(tuple_a)

# Add and remove items 
new.append(6) 
new.pop(3)     

# Convert back into a tuple
tuple_a = tuple(new)
print(tuple_a)  


#set
#in set items are un-ordered

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#False and 0 is considered the same value:
set = {"apple", "banana", "cherry", False, 0, 2}

print(set)
print(len(set))
print(type(set))


#Check if "shwarma" is present in the set:
food = {"shwarma","burger","pizza","chips"}
print("shwarma" in food)
#Check if "pizza" is  not present in the set:
print("pizza" not in food)

#access items in the set
for x in food:
    print(x)

#add items
food.add("coldring")
print(food)
#remove item
food.remove("burger")
print(food)
food.discard("burger")
print(food)
food.clear()
print(food)


