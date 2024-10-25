# Function to create a 2x2 matrix initialized to zeros
def create_matrix():
    return [[0, 0], [0, 0]]


# Function to update a specific element in the matrix
def update_element(matrix, row, col, value):
    matrix[row][col] = value


# Function to display the matrix in 2x2 format without using loops
def display_matrix(matrix):
    print(f"[{matrix[0][0]}, {matrix[0][1]}]")
    print(f"[{matrix[1][0]}, {matrix[1][1]}]")


# Function to transpose the matrix (swap rows and columns)
def transpose_matrix(matrix):
    return [[matrix[0][0], matrix[1][0]], [matrix[0][1], matrix[1][1]]]


# Function to calculate the sum of all elements in the matrix
def sum_of_elements(matrix):
    return matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]


# Function to multiply each element of the matrix by a scalar
def multiply_by_scalar(matrix, scalar):
    matrix[0][0] *= scalar
    matrix[0][1] *= scalar
    matrix[1][0] *= scalar
    matrix[1][1] *= scalar

# Example usage:

# Step 1: Create a matrix
matrix = create_matrix()
print("Initial Matrix:")
display_matrix(matrix)

# Step 2: Update elements
update_element(matrix, 0, 0, 5)  # Update element at (0, 0) to 5
update_element(matrix, 1, 1, 3)  # Update element at (1, 1) to 3
print("\nMatrix after updates:")
display_matrix(matrix)

# Step 3: Transpose the matrix
transposed_matrix = transpose_matrix(matrix)
print("\nTranspose of the matrix:")
display_matrix(transposed_matrix)

# Step 4: Calculate the sum of all elements
matrix_sum = sum_of_elements(matrix)
print(f"\nSum of all elements: {matrix_sum}")

# Step 5: Multiply the matrix by a scalar
multiply_by_scalar(matrix, 2)
print("\nMatrix after multiplying by 2:")
display_matrix(matrix)