import math

a = float(input('Please enter the value of side A of right angle triangle in cms\n'))
b = float(input('Please enter the value of side B of right angle triangle in cms\n'))

result = math.sqrt(pow(a, 2) + pow(b, 2))

print(f'Hypotenues value: {result}')