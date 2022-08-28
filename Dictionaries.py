#Basic dictionary
ages = {'john': 29, 'alex' : 40, 'joe': 33}
print(ages)

#Getting value from key
print(ages['john'])

#Changing value
ages['alex'] = 44
print(ages)

#Removing item
del ages['john']
print(ages)

#keys method- list of dict keys
print(ages.keys())

#values method- list of dict value
print(ages.values())

#items- dict item class that is a list of tuples
print(ages.items())