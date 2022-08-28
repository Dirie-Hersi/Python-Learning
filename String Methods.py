#Lower
my_str = 'HEllo'
print(my_str.lower())

#Upper
print(my_str.upper())

#Capitalize
print(my_str.capitalize())

#Title
multiword = 'This is a multi word sentence'
print(multiword.title())

#split
phrase = 'This is a simple phrase'
words = phrase.split()
print(words)

url = 'https://expample.com/users/jimmy'
user = url.split('/')[-1]
print(url.split('/'))
print(user)

#join
lines = ['First line', 'Second line', 'Third line']
output= '\n'.join(lines)
print(output)

#format
template = "Hello, my name is {}, and I really enjoy {}, have a nice day!"
print(template.format('Dirie', 'Python'))