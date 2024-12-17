def display_menu():
    menu = {
        'Burger': 25.00,
        'Pizza': 38.00,
        'Pasta': 36.00,
        'Salad': 34.00,
        'Soda': 20.00
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item} - P{price:.2f}")

def select_order():
    menu = {
        'Burger': 25.00,
        'Pizza': 38.00,
        'Pasta': 36.00,
        'Salad': 34.00,
        'Soda': 20.00
    }
    items_selected = []
    while True:
        choice = input("Please select an item from the menu (or type 'done' to finish): ")
        if choice.lower() == 'done':
            break
        elif choice in menu:
            items_selected.append(menu[choice])
            print(f"Added {choice} to your order.")
        else:
            print("Invalid choice. Please select a valid item.")
    return items_selected

def process_payment(total_cost):
    while True:
        try:
            cash_rendered = float(input(f"Please enter the amount of cash rendered: P"))
            if cash_rendered >= total_cost:
                change = cash_rendered - total_cost
                print(f"Change: P{change:.2f}")
                break
            else:
                print("Insufficient cash. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    display_menu()
    items_selected = select_order()
    total_cost = sum(items_selected)
    print(f"Total cost: P{total_cost:.2f}")
    process_payment(total_cost)

if __name__ == "__main__":
    main()
