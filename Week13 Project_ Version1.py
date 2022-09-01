from secrets import choice
import string

num_of_instances = input('How many EC2 instances do you want to provision?\n')

department = input('What is your department?\n')

print(f"You have asked to provision {num_of_instances} EC2 instances for the {department} department\n The names are: \n")

for _ in range (int(num_of_instances)):
    print (str(department),''.join([choice(string.ascii_uppercase + string.digits) for _ in range(10)]))