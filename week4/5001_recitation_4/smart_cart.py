def calculate_total_cost(prices, quantities):
    # Check if the lengths of prices and quantities lists are the same
    if len(prices) != len(quantities):
        raise ValueError("Error: Prices and quantities list length mismatch.")
    
    total_cost = 0
    
    # Iterate through both lists
    for price, quantity in zip(prices, quantities):
        try:
            # Try to convert price and quantity to float and int respectively
            item_price = float(price)
            item_quantity = int(quantity)
            
            # Calculate the cost for this item and add to total
            total_cost += item_price * item_quantity
        
        except ValueError:
            # Handle invalid price
            if not isinstance(price, (int, float)):
                print("Warning: Invalid item price skipped.")
            # Handle invalid quantity
            elif not isinstance(quantity, int):
                print("Warning: Invalid item quantity skipped.")
            # Continue with the next item
            continue
    
    print(total_cost)
    return total_cost
    


def test_calculate_total_cost():
    test_cases = [
        # Case 1: Normal case with valid prices and quantities
        {
            "prices": [10.0, 20.0, 30.0],
            "quantities": [1, 2, 3],
            "expected": 140.0
        },
        # Case 2: Prices and quantities list length mismatch
        {
            "prices": [10.0, 20.0],
            "quantities": [1, 2, 3],
            "expected": "ValueError"
        },
        # Case 3: Invalid price (non-numeric)
        {
            "prices": [10.0, "invalid", 30.0],
            "quantities": [1, 2, 3],
            "expected": 100.0
        },
        # Case 4: Invalid quantity (non-numeric)
        {
            "prices": [10.0, 20.0, 30.0],
            "quantities": [1, "invalid", 3],
            "expected": 100.0
        },
        # Case 5: Both invalid price and quantity
        {
            "prices": [10.0, "invalid", 30.0],
            "quantities": [1, "invalid", 3],
            "expected": 100.0
        },
        # Case 6: Empty lists
        {
            "prices": [],
            "quantities": [],
            "expected": 0.0
        }
    ]

    for i, case in enumerate(test_cases):
        prices = case["prices"]
        quantities = case["quantities"]
        expected = case["expected"]
        
        try:
            result = calculate_total_cost(prices, quantities)
            assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        except ValueError as e:
            assert str(e) == "Error: Prices and quantities list length mismatch.", f"Test case {i+1} failed: expected ValueError, got {e}"

    print("All test cases passed!")

# Run the test cases
#test_calculate_total_cost()

prices = [10.0, "invalid", 30.0]
quantities= [1, 2, 3]
calculate_total_cost(prices, quantities)