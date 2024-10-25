"""
4. Displaying Statements

You are given a circle of radius r = 4, and a rectangle of length l = 3 and width w = 5. 
Write a Python program that computes and displays the perimeter and area of both the circle and rectangle.

Expected Output:
The perimeter of the rectangle is 16.0. The area of the rectangle is 15.0.
The perimeter of the circle is 25.1327. The area of the circle is 50.26548.

Hints:
• The formula for the perimeter of a rectangle is 2 × (l + w).
• The formula for the area of a rectangle is l × w.
• The formula for the perimeter (circumference) of a circle is 2 × π × r.
• The formula for the area of a circle is π × r^2 .

Use Python’s math library to access the value of π.
"""

import math

# Given values
circle_radius = 4
rectangle_length = 3
rectangle_width = 5

# Calculate the perimeter and area of the rectangle
rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
rectangle_area = rectangle_length * rectangle_width

circle_perimeter = 2 * math.pi * circle_radius
circle_area = math.pi * circle_radius**2

# Display the results
print(f"The perimeter of the rectangle is {rectangle_perimeter:.1f}.")
print(f"The area of the rectangle is {rectangle_area:.1f}.")
print(f"The perimeter of the circle is {circle_perimeter:.4f}.")
print(f"The area of the circle is {circle_area:.5f}.")
