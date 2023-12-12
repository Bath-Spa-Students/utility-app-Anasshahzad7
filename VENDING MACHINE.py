print("""                                                                                                                                                                                                                                                        
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
""")
class VendingMachine:
    def __init__(self):
        self.products = {
            'cola': {'price': 1.50, 'quantity': 10},
            'chips': {'price': 1.00, 'quantity': 15},
            'candy': {'price': 0.75, 'quantity': 20},
            'mango juice' : {'price' : 2.00, 'quantity' : 1}
        }
        self.balance = 0.0

    def display_products(self):
        print("Available Products:")
        for product, details in self.products.items():
            print(f"{product.capitalize()}: ${details['price']} - Quantity: {details['quantity']}")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance:.2f}")

    def select_product(self, product):
        if product in self.products:
            if self.products[product]['quantity'] > 0 and self.balance >= self.products[product]['price']:
                self.products[product]['quantity'] -= 1
                self.balance -= self.products[product]['price']
                print(f"Dispensing {product.capitalize()}... Enjoy!")
            else:
                print("Insufficient funds or out of stock.")
        else:
            print("Invalid product selection.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0.0
        else:
            print("No change to return.")

# Example usage:
if __name__ == "__main__":
    vending_machine = VendingMachine()

    while True:
        print("\nWelcome to the Extra Good Vending Machine!")
        vending_machine.display_products()

        choice = input("\nEnter product name (or 'exit' to quit): ").lower()

        if choice == 'exit':
            break

        if choice == 'admin':  # Secret admin code to restock products
            for product in vending_machine.products:
                vending_machine.products[product]['quantity'] = 10
            print("Admin restocked products.")

        elif choice in vending_machine.products:
            amount = float(input("Insert money (in dollars): "))
            vending_machine.insert_money(amount)
            vending_machine.select_product(choice)

        else:
            print("Invalid choice. Please try again.")
    
    vending_machine.return_change()
