import sys

value1, operation, value2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

if operation == 'add':
    print('Sum: ',value1+value2)
elif operation == 'diff':
    print('Difference: ',value1-value2)
elif operation == 'div':
    print('Quotient: ',value1/value2)
    print('Remainder: ',value1%value2)
elif operation == 'prod':
    print('Product: ',value1*value2)