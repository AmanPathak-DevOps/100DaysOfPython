pwd = input('Enter a password and I will tell the password is strong or weak \n')

capital_letter_present = any(char.isupper() for char in pwd)
number_present_present = any(char.isdigit() for char in pwd)
special_symbol_present = any(not char.isalnum() for char in pwd)


if len(pwd) < 8:
    print('Password is weak')
elif capital_letter_present == False:
    print('Not able to find any capital letter in your password. Please create a strong password!')
elif number_present_present == False:
    print('Not able to find any numeric value in your password. Please create a strong password!')
elif special_symbol_present == False:
    print('Not able to find any special character in your password. Please create a strong password!')
else: 
    print('Great, Your Password looks great and very strong :)')