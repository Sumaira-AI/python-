

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
