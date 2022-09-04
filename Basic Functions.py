#Basic function
def add_two(num):
    return num + 2
    
result = add_two(3)
print(result)

def add(num1, num2):
    return num1 + num2

output = add(6,8)
print(output)


#Different ways of passing in arguments
def contact_card(name, age, car_model):
    return f"{name} is {age} and drives a {car_model}"
    
print(contact_card("Joe", 33, "Aston Martin"))
print(contact_card(age=70, car_model="Lambo", name="Stanley"))


def can_drive(age,driving_age=16):
    return age >= driving_age
    
print(can_drive(14))













