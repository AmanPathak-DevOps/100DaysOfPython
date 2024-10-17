year = int(input('Enter the year to check whether its leap or not '))

if (year % 4 == 0):
    print(f'Year {year} is a Leap')
else: 
    print(f'Year {year} is not a Leap')