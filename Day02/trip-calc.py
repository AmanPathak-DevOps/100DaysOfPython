print('----------------------------------')
print('Welcome to the Trip Calculator!!!')

money = float(input('How much money you guys spent?(in ₹)\n'))

tip = float(input('How much tip you have given in the Restaurant?(in ₹)\n'))

number_of_guys = int(input('How many guys you are?\n'))

print('----------------------------------')
print('Share for Each Guy ',(money+tip)/number_of_guys)