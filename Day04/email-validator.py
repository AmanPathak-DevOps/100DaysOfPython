email = input('Enter your email id and I will tell you whether your mail id is valid or not :) ')

if email.find('@') != -1 and email.endswith('com') == True: 
    print('Valid')
else: 
    print('Not a valid mail id :(')