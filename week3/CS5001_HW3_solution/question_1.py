# Inventory system using a dictionary
# The key is the item name, and the value is the list of quantities from various warehouses.
inventory = {}


# Function to add a new item to the inventory
def add_item(name, quantities):
    if name in inventory:
        print(f"Item '{name}' already exists. Use update to add quantities.")
    else:
        inventory[name] = quantities
        print(f"Item '{name}' added successfully!")


# Function to update an existing item with a new warehouse quantity
def update_item(name, new_quantity):
    if name in inventory:
        inventory[name].append(new_quantity)
        print(f"Added new warehouse quantity {new_quantity} to item '{name}'.")
    else:
        print(f"Item '{name}' does not exist in the inventory.")


# Function to remove an item by name
def remove_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from inventory.")
    else:
        print(f"Item '{name}' not found in the inventory.")


# Function to display the quantities of a specific item by its name
def display_item(name):
    if name in inventory:
        print(f"Item: {name}, Quantities: {inventory[name]}")
    else:
        print(f"Item '{name}' not found in the inventory.")


# Function to display all items in the inventory along with their quantities
def display_all_items():
    if inventory:
        print("Inventory:")
        for item, quantities in inventory.items():
            print(f"Item: {item}, Quantities: {quantities}")
    else:
        print("Inventory is empty.")


# Sample menu to interact with the inventory system
def inventory_menu():
    while True:
        print("\nInventory Menu:")
        print("1. Add new item")
        print("2. Update existing item")
        print("3. Remove an item")
        print("4. Display item quantities")
        print("5. Display all items")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter the item name: ")
            quantities = list(map(int, input("Enter quantities for warehouses (separate by spaces): ").split()))
            add_item(name, quantities)
        elif choice == '2':
            name = input("Enter the item name to update: ")
            new_quantity = int(input("Enter the new warehouse quantity: "))
            update_item(name, new_quantity)
        elif choice == '3':
            name = input("Enter the item name to remove: ")
            remove_item(name)
        elif choice == '4':
            name = input("Enter the item name to display: ")
            display_item(name)
        elif choice == '5':
            display_all_items()
        elif choice == '6':
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice, please select again.")


# Running the inventory menu
if __name__ == '__main__':
    inventory_menu()