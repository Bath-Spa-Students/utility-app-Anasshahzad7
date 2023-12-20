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
        self.items = {
            1: {"name": "dew6", "price": 1.50},
            2: {"name": "ice cream", "price": 1.00},
            3: {"name": "Chocolate", "price": 0.75},
            4: {"name": "chips", "price": 0.50},
            5: {"name": "coco cola", "price": 50},
            6: {"name": "sandwich", "price": 3.00},
            7: {"name": "water", "price": 1.00},
            # Add more items as needed
        }

    def display_items(self):
        print("Available Items:")
        for item_num, item_info in self.items.items():
            print(f"{item_num}. {item_info['name']} - ${item_info['price']}")

    def purchase_item(self, item_number, amount_inserted):
        if item_number in self.items:
            selected_item = self.items[item_number]
            item_price = selected_item["price"]

            if amount_inserted >= item_price:
                change = amount_inserted - item_price
                print(f"Enjoy your {selected_item['name']}! Your change is ${change:.2f}")
            else:
                print("Insufficient cash. Please insert more money.")
        else:
            print("Invalid item number. Please select a valid item number.")

# Example Usage:
if __name__ == "__main__":
    vending_machine = VendingMachine()

    vending_machine.display_items()

    try:
        item_number = int(input("Enter the number of the item you want to purchase: "))
        amount_inserted = float(input("Insert money: $"))
        
        vending_machine.purchase_item(item_number, amount_inserted)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
