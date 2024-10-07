import csv
from prettytable import PrettyTable

# Updated menu with Singaporean dishes
menu = {
    'Hainanese Chicken Rice': 5.0,
    'Chilli Crab': 25.0,
    'Laksa': 6.5,
    'Satay': 8.0,
    'Bak Kut Teh': 7.5,
    'Kaya Toast': 3.0,
    'Char Kway Teow': 6.0,
    'Roti Prata': 4.0,
    'Mee Rebus': 5.5,
    'Nasi Lemak': 6.0
}

order = []

def main():
    print("Welcome to Singh's restaurant >")
    print("Have a look at the menu and order what you want ")
    display_menu()
    take_order(menu, order)
    review_order()
    bill = calculate_bill(menu, order)
    print(f"Total Bill: ${bill:.2f}")

def display_menu():
    # Display the menu with index
    print("Menu:")
    for index, (item, price) in enumerate(menu.items(), 1):
        print(f"{index}. {item}: ${price:.2f}")

def take_order(menu, order):
    while True:
        try:
            index = input('Enter item number (press e to finish ordering): ')
            if index.lower() == 'e':
                save_order(order)
                break
            index = int(index)
            if 1 <= index <= len(menu):
                item = list(menu.keys())[index - 1]
                quantity = int(input(f'Enter quantity for {item}: '))
                order.append((item, quantity))
            else:
                print("Invalid menu number, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

def save_order(order):
    with open('orders.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item', 'Quantity'])
        for item, quantity in order:
            writer.writerow([item, quantity])

def review_order():
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != ['Item', 'Quantity']:
            raise Exception("CSV file is corrupted")

        items = []
        for row in reader:
            item = row[0]
            quantity = int(row[1])
            items.append((item, quantity))

        x = PrettyTable(header)
        for item, quantity in items:
            x.add_row([item, quantity])

        print("Your Order is: ")
        print(x)

def calculate_bill(menu, order):
    total = 0
    for item, quantity in order:
        total += menu[item] * quantity
    print("Thank you very much for ordering food from our restaurant. Visit again!")
    return total

if __name__ == '__main__':
    main()
