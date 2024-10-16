# Ask the user name until he/she didn't tell his/her name
def enter_name():
    name = input("What is Your Name? ")
    check_skip(name)

def check_skip(name):
    is_skip = bool(name)
    if is_skip:
        print(f'Your name: {name}')
    else:
        print(f'You didnt enter any name! Please enter the name')
        print('*************************************************')
        enter_name()
    
enter_name()