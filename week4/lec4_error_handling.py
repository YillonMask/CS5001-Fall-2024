class SnackNotAvailableError(Exception):
    pass

class InsufficientMoneyError(Exception):
    pass

def vending_machine():
    # Dictionary of available snacks and their prices
    snacks = {
        "chips": 1.50,
        "chocolate": 2.00,
        "soda": 1.25,
        "candy": 0.75
    }

    try:
        # Get user input
        selected_snack = input("Enter the snack you want to purchase: ").lower()
        
        # Check if snack is available
        if selected_snack not in snacks:
            raise SnackNotAvailableError("Snack not found in the vending machine.")
        
        # Get user's money
        money = float(input("Enter the amount of money you have: $"))
        
        # Check if user has enough money
        if money < snacks[selected_snack]:
            difference = snacks[selected_snack] - money
            raise InsufficientMoneyError(f"You need ${difference:.2f} more to purchase this snack.")
        
        # Process the purchase
        change = money - snacks[selected_snack]
        print(f"Here's your {selected_snack}! Your change is ${change:.2f}")

    except SnackNotAvailableError as e:
        print(f"Error: {e}")
    except InsufficientMoneyError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the money.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the vending machine program
vending_machine()