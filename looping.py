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
    

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
    
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)
