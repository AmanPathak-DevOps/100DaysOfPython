try:
    age = int(input("What is your Age?\n"))
    print('------------------------------')
    print('You Age is ',age)
except ValueError:
    print('Value must be Integer Only!!!!')