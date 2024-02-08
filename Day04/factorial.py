value = int(input('Enter the number to perform the factorial on it\n'))

i = 1
temp = 1
while i<=value:
    temp=temp*i
    i+=1
    
print(temp)