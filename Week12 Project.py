#Empty List
aws_services= []
print("The number of items in this list is", len(aws_services))

#Adding Services
aws_services.insert(0, 'Amazon Aurora')
aws_services.insert(1, 'DynamoDB')
aws_services.insert(2, 'EC2')
aws_services.insert(3, 'Cloud9')
aws_services.insert(4, 'S3')

#Sorting and Printing List
aws_services.sort()
print(aws_services)

#Printing length of List
print("The number of items in this list is", len(aws_services))

#Removing first and last items from list
del aws_services[0]
del aws_services[-1]
print(aws_services)
print("The number of items in this list is", len(aws_services))