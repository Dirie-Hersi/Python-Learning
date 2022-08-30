if 'a' < 'b':
    print("Condition was true")
    
if 'b' <= 'b':
    print("Condition was true")
    
if False:
    print("Was true")
else:
    print("Was false")
    
if 'b' < 'a':
    print("This is true")
elif 'c' < 'd':
    print("Second condition is true")
else:
    print("no condition was true")
    
    

name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long!")
elif len(name) == 5:
    print("Your name is exactly 5 characters long!")
else:
    print("Your name is short!")
    
    