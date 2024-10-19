mob_number = input('Enter the nubmber ')

if len(mob_number) < 10 and len(mob_number) > 10:
    print('Number is Invalid. Please enter again!! :(')
else:
    head_num = f"({mob_number[:3]}) "
    num = head_num + mob_number[3:6] + '-' + mob_number[6:10]
    print(num)