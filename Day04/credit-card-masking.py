cc_num = input('Enter your credit card number ')


if len(cc_num) < 16:
    print(cc_num)
elif len(cc_num) == 16:
    last_four_num = cc_num[-4:]

    # replace first 12 numbers with *
    masker_num = '*' * (len(cc_num) -4)

    final_cc_num = masker_num + last_four_num
    print(final_cc_num)
else:
    print('Entered Invalid Credit Card details! :(')