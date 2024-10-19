email = input('Enter your mail id ')

username,domain = email.split('@')
if len(username) < 4:
    print('No need to mask')
    print(username)
else:
    masking_username = username[:3] + '*' * (len(username) -4 ) + username[-3:]
    print('After masking the username')
    print(masking_username)