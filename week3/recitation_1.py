# Contact Book Manager

# Initialize the contact book as an empty dictionary
contact_book = {}


# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone_numbers = input("Enter phone number(s), separated by commas: ").split(",")
    phone_numbers = [num.strip() for num in phone_numbers]

    if name in contact_book:
        print(f"Contact '{name}' already exists.")
    else:
        contact_book[name] = phone_numbers
        print(f"Contact '{name}' added successfully.")


# Function to update an existing contact by adding a new phone number
def update_contact():
    name = input("Enter the contact name you want to update: ").strip()

    if name in contact_book:
        new_phone_number = input("Enter the new phone number to add: ").strip()
        contact_book[name].append(new_phone_number)
        print(f"Phone number '{new_phone_number}' added to contact '{name}'.")
    else:
        print(f"Contact '{name}' does not exist.")


# Function to remove a contact by name
def remove_contact():
    name = input("Enter the contact name you want to remove: ").strip()

    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"Contact '{name}' does not exist.")


# Function to display phone numbers for a specific contact by name
def display_contact():
    name = input("Enter the contact name you want to display: ").strip()

    if name in contact_book:
        print(f"Phone numbers for '{name}': {', '.join(contact_book[name])}")
    else:
        print(f"Contact '{name}' not found.")


# Function to display all contacts
def display_all_contacts():
    if contact_book:
        print("All contacts:")
        for name, phone_numbers in contact_book.items():
            print(f"{name}: {', '.join(phone_numbers)}")
    else:
        print("No contacts available.")


# Main menu to interact with the contact book
def main_menu():
    while True:
        print("\n--- Contact Book Manager ---")
        print("1. Add new contact")
        print("2. Update existing contact")
        print("3. Remove a contact")
        print("4. Display contact by name")
        print("5. Display all contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            remove_contact()
        elif choice == "4":
            display_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            print("Exiting Contact Book Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main_menu()
