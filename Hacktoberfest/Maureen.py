name = input("What's your name?")
order = input("What would you like to order?")
milk = input ("Would you like whole milk or almond milk?")

def cost(order):
    if order == 'cake':
        price = 2
    elif order == 'English breakfast':
        price = 6
    else:
        price = 5
    return price

total = cost(order)

print(f"Hello {name}, your order is: {order} and the type of milk ordered is {milk}. The  cost is: {total}")
