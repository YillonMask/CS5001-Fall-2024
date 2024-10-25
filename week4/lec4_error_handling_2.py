def calculate_price_per_slice(total_price, number_of_slices):
    try:
        price_per_slice = total_price / number_of_slices
        print(f'The price for each slice is {price_per_slice}!')
    except ValueError:
        print("Invalid input! Please enter numeric values for price and number of slices.")
    except ZeroDivisionError:
        print("Number of slices cannot be zero. Please enter a valid number of slices.")
    except ArithmeticError as e:
        print(f"An arithmetic error occurred: {e}")

def main():
    try:
        total_price = float(input("Please input the price of the whole pizza: "))
        number_of_slices = float(input("Please input the number of slices of pizza: "))
        calculate_price_per_slice(total_price, number_of_slices)
    except ValueError as e:
        print(f"Invalid input! {e}")

main()