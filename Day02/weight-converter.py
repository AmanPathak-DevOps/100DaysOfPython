print('There are two types of weight converter we provide\n 1. Pounds to Kilogram\n 2. Kilogram to Pounds')
choice = input('Please enter the type of weight converter do you want? (1 OR 2) ')
weight = float(input("Please enter your weight! "))

if choice == '1': 
    weight = weight / 2.205
    print(f'Weight converted in Kilogram: {weight}')
elif choice == '2':
    weight = weight * 2.205
    print(f'Weight converted in Pounds: {weight}')
else:
    print('Oops! You entered the wrong choice. Please enter the correct choice:)')