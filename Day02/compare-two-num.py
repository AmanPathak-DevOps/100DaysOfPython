num1, num2 = map(int, input('Enter two numbers! (ex- 34 89)\n').split())
 
print('Now I will tell you which one is larget')

if(num1 > num2):
    print(f'Num1={num1} is larger than Num2={num2}')
elif(num1 < num2):
    print(f'Num2={num2} is larger than Num1={num1}')
else: 
    print('Both are equal!')