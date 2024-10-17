operator = input('Please Enter an Operator (+ -  * /)! ')
num1 = float(input('Enter the value for num1 '))
num2 = float(input('Enter the value for num2 '))

if operator == '+':
    result = num1 + num2
    print(f'Sum of two values are: {result}')
elif operator == '-':
    result = num1 - num2
    print(f'Difference between two values are: {result}')
elif operator == '*':
    result = num1 * num2
    print(f'Product of two values are: {result}')
elif operator == '/':
    result = num1 / num2
    print(f'Quotient after dividing value for {num1}/{num2} is: {result}')
else:
    print('You entered wrong input! Please enter correct input. Thanks:)!')