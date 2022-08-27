#Basic List
my_list = [1,2,3,4,5]
print(my_list)
print(len(my_list))

#List with mixed types
other_list = ['a', 1, 2.0, False]
print(other_list)
print(len(other_list))

#Use slicing to get subsection of a list
print(my_list[0:2])
print(other_list[0::2])

#Lists are mutable and can be modified
my_list[0] = 'a'
print(my_list)

#Concatenate List
my_list += [8,9,10]
print(my_list)

#Assigning new list items to a slice
my_list[1:3] = ['b','c']
print(my_list)

#Remove items from a list
del my_list[0]
print(my_list)


