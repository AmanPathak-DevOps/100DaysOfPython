age = int(input('Enter your age to check whether you are eligible to vote or not '))

if (age < 18 and age > 0):
    print('Sorry! You are not eligible for voting. Come again once you crossed 18')
elif (age > 18 ):
    print('Great! You can part of this democrate exercise of this country :)')
else: 
    print('Incorrect Input!:(')