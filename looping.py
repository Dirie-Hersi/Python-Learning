count = 1
while count <= 4:
    print("Looping!")
    count +=1
    
#List    
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)

#Tuple
point = (1,2,3)
for value in point:
    print(value)
    
#Dictionary
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)
    
#Dictionary keys + values in loop
for key, value in ages.items():
    print(key, value)
    
#String
for letter in 'my_string':
    print(letter)
    
    
#Nesting Loops
counter = 1
while counter <= 25:
    if counter % 4 == 0:
        print(counter)
    counter +=1
    
counter = 1
while counter <= 100:
    if counter % 5 == 0:
        print(counter)
    counter +=1
    
#Continue
count = 0
while count < 10:
    if count % 2 ==0:
        count +=1
        continue
    print(f"We're counting odd numbers: {count}")
    count +=1
    
print()

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
    
print()

colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)

print()

count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")
    
print()

colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print('Orange is in the list')
        break
else:
    print('Orange is not in the list')
    
    
print()
 
  #Range
  
myrange = range(10)
print(list(myrange))

count = 1
while count <= 4:
    print('looping')
    count += 1
    
for _ in range(4):
    print('looping')
    
#List comprehensions

colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
print(uppercase_colors)

print()

#list comprehension
uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors =[color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)