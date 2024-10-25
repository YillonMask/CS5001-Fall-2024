import math

# Fun Example 2
def calculate_roots(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"The roots are real and different: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"The roots are real and identical: {root}"
    else:
        return "The roots are complex and do not have real solutions."

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

result = calculate_roots(a, b, c)
print(result)


# Fun Example 3
def calculate_tip(total_bill, tip_percentage):
    # Calculate the tip amount
    tip_amount = total_bill * (tip_percentage / 100)
    # Calculate the total amount including the tip
    total_with_tip = total_bill + tip_amount
    return tip_amount, total_with_tip

try:
    total_bill = float(input("Enter the total bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage you want to give: "))

    tip_amount, total_with_tip = calculate_tip(total_bill, tip_percentage)
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount including tip: ${total_with_tip:.2f}")
except ValueError:
    print("Please enter valid numerical values for the bill and tip percentage.")


# Fun Example 4
def calculate_dti(annual_income, total_debt):
    monthly_income = annual_income / 12
    monthly_debt_payment = total_debt / 12
    dti_ratio = (monthly_debt_payment / monthly_income) * 100
    return dti_ratio

def check_loan_eligibility(annual_income, total_debt, dti_threshold=36):
    dti_ratio = calculate_dti(annual_income, total_debt)
    if dti_ratio < dti_threshold:
        return f"Eligible for a loan. Your DTI ratio is {dti_ratio:.2f}%."
    else:
        return f"Not eligible for a loan. Your DTI ratio is {dti_ratio:.2f}%."

try:
    annual_income = float(input("Enter your annual income: $"))
    total_debt = float(input("Enter your total existing debt: $"))
    dti_threshold = float(input("Enter the maximum DTI ratio allowed for eligibility (e.g., 36): "))
    result = check_loan_eligibility(annual_income, total_debt, dti_threshold)
    print(result)
except ValueError:
    print("Please enter valid numerical values for the income, debt, and DTI threshold.")



# Fun Example 5
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number between 1 and 10.")

# Start the game
guess_the_number()



# Fun Example 6
larger = lambda x, y: x if x > y else y

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"


# Fun Example 7
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  #"olleh"


# Fun Example 8
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = 10
print("Fibonacci sequence:")
for i in range(n_terms):
    print(fibonacci(i))

