file_name = input('Enter the file and I will tell you the type of file ')



extension_present = file_name.rfind(".")

if extension_present == -1:
    print('No extension found!')
else:
    extension = file_name.split(".")

    print(f'File extension found which is: {extension[-1]}')