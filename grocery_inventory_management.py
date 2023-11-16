# Define an empty inventory dictionary to store items
inventory = {}

# Function to add a new item to the inventory
def add_item():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    inventory[item_name] = {"quantity": quantity, "price": price}
    print("Item added successfully!")

# Function to update the quantity of an existing item
def update_quantity():
    item_name = input("Enter the item name: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name]["quantity"] = new_quantity
        print("Quantity updated successfully!")
    else:
        print("Item not found in the inventory.")

# Function to view the current inventory
def view_inventory():
    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        print(f"Item: {item}\t Quantity: {details['quantity']}\t Price: {details['price']}")
    print()

# Function to remove an item from the inventory
def remove_item():
    item_name = input("Enter the item name: ")
    if item_name in inventory:
        del inventory[item_name]
        print("Item removed successfully!")
    else:
        print("Item not found in the inventory.")

# Main program loop
while True:
    print("\n*** Grocery Store Inventory Management ***")
    print("1. Add new item")
    print("2. Update quantity")
    print("3. View inventory")
    print("4. Remove item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_item()
    elif choice == 2:
        update_quantity()
    elif choice == 3:
        view_inventory()
    elif choice == 4:
        remove_item()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye! Thank you for using the Grocery Store.")
