import math

name = input("Welcome to the GC Fruit Market!\nWhat is your name?\n> ")

fruit_prices = {
    "Apple": 2,
    "Grape": 1,
    "Orange": 3
}

def calculate_receipt(cart):
    subtotal = sum(cart[fruit] * fruit_prices[fruit] for fruit in cart)
    tax = subtotal * 0.05
    total = subtotal + tax
    return subtotal, tax, total


cart = {}

while True:
    print(f"\nWelcome {name}. Which fruit would you like to buy?")
    for index, (fruit, price) in enumerate(fruit_prices.items(), start=1):
        print(f"{index}. {fruit} ${price}")

    try:
        choice = int(input("> "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice in range(1, len(fruit_prices) + 1):
        selected_fruit = list(fruit_prices.keys())[choice - 1]

        try:
            quantity = int(input(f"How many {selected_fruit}(s) would you like to buy? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if selected_fruit in cart:
            cart[selected_fruit] += quantity
        else:
            cart[selected_fruit] = quantity
    else:
        print("Invalid choice. Please choose a number from the list.")
        continue

    if input("Would you like to buy another piece of fruit? y/n\n> ").lower() != 'y':
        break


subtotal, tax, total = calculate_receipt(cart)
print(f"\nOrder for {name}")
for fruit, quantity in cart.items():
    print(f"{quantity} {fruit}(s) at ${fruit_prices[fruit]} apiece")
print(f"Subtotal: ${subtotal:.2f}")
print(f"5% Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
