first_name = input('What is your First Name ?\n: ')
print('')
last_name = input('Enter Your LastName \n: ')

#output = f'Hello, {first_name} {last_name}
#output = 'Hello, ' +first_name+' '+last_name
output = 'Hello, {1} {0}'.format(first_name, last_name)
#output = f'Hello, {first_name} {last_name}'
print(output)