smallest = lambda numbers: min(numbers)

square = lambda x: x * x

round_float = lambda x: round(x, 2)

average = lambda x, y, z: (x + y + z) / 3

# lower function convert char to lowercase
is_vowel = lambda char: char.lower() in "aeiou"

# key=len means the max function compares elements based on their length.
longest = lambda strings: max(strings, key=len) 

# Example usage of the lambda functions

# 1. Find the smallest number in a list
numbers = [3, 1, 4, 1, 5, 9]
print(smallest(numbers))  # Output: 1

# 2. Return the square of an integer
print(square(5))  # Output: 25

# 3. Round a float to two decimal places
print(round_float(3.14159))  # Output: 3.14

# 4. Find the average of three numbers
print(average(3, 4, 5))  # Output: 4.0

# 5. Check if a character is a vowel
print(is_vowel("a"))  # Output: True
print(is_vowel("b"))  # Output: False

# 6. Find the longest string in a list
strings = ["apple", "watermelon", "cherry"]
print(longest(strings))  # Output: watermelon
