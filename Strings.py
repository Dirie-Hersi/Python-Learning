# Now let's experiment with strings

# Single quoted string

'This is a single quote'

#Double quoted strings

"Double quoted strings"

#Multi-line

'''
This is a triple quoted
multi line string
'''

# Adding strings

first_str = "Pass"
second_str= "word"

print(first_str + second_str)

# This actually works ??!

print("Ha" * 4)

print("\nHa" * 4)

#find() Method- Returns first occurence of the specified value

print("my_string".find('in'))

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)



# Returning lowercase and uppercase
print("teSTiNG".lower())

print("testing".upper())

# New Line Escape

print("New\nLine")
