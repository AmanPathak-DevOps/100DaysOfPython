username = input('Enter your username and I will validate whether its meet with our requirements or not ')

# print(help(str))
if len(username) > 12:
    print('Length of your username is too long. Keep it in 12 characters only :(')
elif not username.find(" ") == -1:
    print('You have added spaces in your username which is not good :(')
elif not username.isalpha():
    print('You have added digits in your username which is not good :(')
else:
    print(f'Welcome {username} :)')