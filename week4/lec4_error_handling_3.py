def calculate_total_cost(prices):
    total_cost = 0

    for item in prices:
        try:
            price = float(item)
            total_cost += price
        except (ValueError, TypeError):
            print("Warning: Invalid item price skipped.")

    return total_cost


# Test the function
if __name__ == "__main__":
    # Test case 1: All valid prices
    prices1 = [10.99, 5.50, 3.75, 8.25]
    print(f"Total cost: ${calculate_total_cost(prices1):.2f}")

    # Test case 2: Some invalid prices
    prices2 = [10.99, "5.50", 3.75, "invalid", 8.25, [2.50]]
    print(f"Total cost: ${calculate_total_cost(prices2):.2f}")
