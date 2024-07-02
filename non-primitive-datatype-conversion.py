#Type Conversion to Tuples and Lists

a_tuple = ('a', 1) ,('f', 2), ('g', 3)
b_list = [1,2,3,4,5]

print(tuple(b_list))
print(list(a_tuple))

#-------------------------------------------------------------------------

# You can also convert a string into a list or a tuple. 
dessert = 'Cake'

# # Convert the characters in a string to individual items in a tuple
print(tuple(dessert))
# # Convert a string into a list
print(list(dessert))

# # Convert a string into a list and also we can do append
dessert_list = list(dessert)
dessert_list.append('s')
print(dessert_list)


#----------------------------------------------------------------------------

# Type Conversion to Dictionaries, and Sets

a_tuple = ('a', 1) ,('f', 2), ('g', 3)
b_list = [1,2,3,4,5]

print(dict(a_tuple))
print(set(b_list))



