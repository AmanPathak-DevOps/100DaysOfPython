iteration = int(input("Enter the iteration to print the fibonacci series\n"))

first = 0
second = 1
i = 1

print('The Fibonacci Series is here')
print(first, second, end=" ")
while i<=iteration-2:
    third = first + second
    print(third, end=" ")
    first = second
    second = third
    i+=1