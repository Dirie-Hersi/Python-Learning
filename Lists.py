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

#Using append- adds to end of list
my_list.append(100)
print(my_list)

#Using insert- choose position of item that will be inserted
my_list.insert(0,'a')
print(my_list)

#Use index to return position of item
my_list.index('c')


#In and Not in examples

#my_list = [1,2,3]
#4 in my_list
#False

#my_list= [1,2,3]
#4 not in my_list
#True

#Sort list
my_list = [1,3,4,8,2]
print(sorted(my_list))

#Reverse sort
print(list(reversed(sorted((my_list)))))


#Matrix
my_matrix = [[1,2,3],
            [ 4,5,6]]

print(my_matrix)


