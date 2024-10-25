# Fun Example 1
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


guess_the_number()


# Fun Example 2

# 1 Lambda function that takes two numbers and returns the larger of the two
larger = lambda x, y: x if x > y else y
print(larger(5, 10))  # Output: 10

# 2 Lambda function to check if an integer is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd

# 3 Lambda function that takes a string and returns its length
string_length = lambda s: len(s)
print(string_length("hello"))  # Output: 5

# 4 Lambda function that takes two numbers and returns their product
product = lambda x, y: x * y
print(product(3, 4))  # Output: 12

# 5 Lambda function that takes a number and returns True if it is a multiple of 5, otherwise returns False
is_multiple_of_5 = lambda x: x % 5 == 0
print(is_multiple_of_5(10))  # Output: True
print(is_multiple_of_5(7))   # Output: False

# 6 Lambda function that takes two strings and returns the one that comes first alphabetically
first_alphabetically = lambda s1, s2: s1 if s1 < s2 else s2
print(first_alphabetically("apple", "banana"))  # Output: apple
