# Exercises 1
def triangle(n):
    i = n
    while(i > 0):
        print("* " * (n-i+1))
        i-=1

triangle(5)


# Exercises 2
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

fibonacci_series(10)

# Exercises 3

# 1. Program that searches for a specific value in a list
def search_value(value, lst):
    for item in lst:
        if item == value:
            print(f"Value {value} found in the list!")
            break
    else:
        print(f"Value {value} is not in the list.")

search_value(5, [1, 2, 3, 4, 5, 6])  # Output: Value 5 found in the list!
search_value(10, [1, 2, 3, 4, 5, 6])  # Output: Value 10 is not in the list.

# 2. Program to check if a number is prime
def is_prime(number):
    if number < 2:
        print("Not prime")
        return

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

is_prime(11)  # Output: Prime
is_prime(4)  # Output: Not prime

# 3. Program that checks if all numbers in a list are positive
def check_all_positive(lst):
    for num in lst:
        if num < 0:
            print("Found a negative number. List is not all positive.")
            break
    else:
        print("All positive")

check_all_positive([1, 2, 3, 4, 5])  # Output: All positive
check_all_positive([1, 2, -3, 4, 5]) # Output: Found a negative number. List is not all positive.

# 4. Program simulating an autonomous vehicle detecting obstacles
def check_for_obstacles(sensors):
    for sensor in sensors:
        if sensor == "obstacle":
            print("Obstacle detected, stop the car!")
            break
    else:
        print("No obstacles, continue driving.")

check_for_obstacles(["clear", "clear", "obstacle", "clear"])  # Output: Obstacle detected, stop the car!
check_for_obstacles(["clear", "clear", "clear"])              # Output: No obstacles, continue driving.

