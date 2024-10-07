import csv
from prettytable import PrettyTable

# Updated menu with Singaporean dishes
menu = {
    'Hainanese Chicken Rice': 5.0,
    'Singapore Chilli Crab': 25.0,
    'Katong Laksa': 6.5,
    'Satay': 8.0,
    'Bak Kut Teh': 8.0,
    'Kaya Toast': 3.0,
    'Char Kway Teow': 5.0,
    'Roti Prata': 4.0,
    'Mee Rebus': 5.5,
    'Nasi Lemak': 6.0,
}

order = []

def main():
    print("=============================")    
    print("WELCOME TO SINGAPORE")
    print("=============================")  
    print("PLEASE HAVE A LOOK AT OUR SPECIAL DISHES!")
    print("\n")  
    display()
    take_o(menu, order)
    review_order()
    bill = calculate_bill(menu, order)
    print(f"Total Bill: ${bill:.2f}")

def display():
    # Display the menu with index
    print("Menu:")
    for index, (item, price) in enumerate(menu.items(), 1):
        print(f"{index}. {item}: ${price:.2f}")

def take_o(menu, order):
    while True:
        try:
            index = input('Enter Item Number (press e to finish ordering): ')
            if index.lower() == 'e':
                save_order(order)
                break
            index = int(index)
            if 1 <= index <= len(menu):
                item = list(menu.keys())[index - 1]
                quantity = int(input(f'Enter Quantity for {item}: '))
                order.append((item, quantity))
            else:
                print("Not Found, Please Try Again.")
        except ValueError:
            print("Invalid Input, Please Enter a Valid Number.")
            continue

def save_order(order):
    with open('Orders.csv', 'w', newline='') as file:
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

        print("Your Final Order: ")
        print(x)

def calculate_bill(menu, order):
    total = 0
    for item, quantity in order:
        total += menu[item] * quantity
    print("=======================================")  
    print("THANK YOU FOR COMING, SEE YOU SOON!!!")
    return total

if __name__ == '__main__':
    main()
