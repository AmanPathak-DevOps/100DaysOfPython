sentence = input('Enter a sentence ')

split = sentence.split(' ')
reverse_list = split[::-1]

reverse_string = " ".join(reverse_list)
print(f'Reverse sentence: {reverse_string}')