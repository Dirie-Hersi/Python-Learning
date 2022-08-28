#Tuples are immutable

my_tuple=(4.0,5.0,6.0)
my_second_tuple = (7.0,8.0,9.0)

print(my_tuple)
print(my_second_tuple)

x, y, z = my_tuple
print(x,y,z)

#List in a Tuple

my_list = [1,2,3]
my_tuple = (my_list, 1)
print(my_tuple)

#Tuple in a List
other_list = [1,2, my_tuple]
print(other_list)