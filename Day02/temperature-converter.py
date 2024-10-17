choice = input("Is this the temperature in Celsius or Fahrenhiet? (C or F) ")

if choice == 'F':

    temp = float(input('Enter the temperature in Fahrenhiet '))
    print('Converting temperature from Fahrenhiet to Celsius... :) ')

    temp = (temp - 32) * 5/9
    print(f'Temperature in Celsius is: {temp}')

elif choice == 'C':
    
    temp = float(input('Enter the temperature in Celsius '))
    print('Converting temperature from Celsius to Fahrenhiet... :) ')

    temp = temp * (9/5) + 32
    print(f'Temperature in Fahrenhiet is: {temp}')
