item = input('Please write the item list here! ')
price = float(input('What is the price of the item? '))
quantity = int(input('How much quantity of the purchase? '))

final_price = price * quantity

print(f'The item you bought {item}')
print(f'Total Price: {final_price}')