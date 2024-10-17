score = float(input('Enter your percentage got in your class. I will tell you the grades:) '))

if (score > 90):
    print('Grade A')
elif (score >= 80 and score <= 90):
    print('Grade B')
elif (score >= 70 and score < 80):
    print('Grade C')
elif (score >= 60 and score < 70):
    print('Grade D')
else:
    print('Fail')