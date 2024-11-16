import numpy as np

# Exercise 1
# Define the size n (for example, n=5)
n = 5

# Create even numbers array (0 to 2n-2)
even_numbers = np.arange(0, 2*n, 2)

# Create odd numbers array (1 to 2n-1)
odd_numbers = np.arange(1, 2*n, 2)

# Stack the arrays vertically
result = np.vstack((even_numbers, odd_numbers))

# Print the resulting array
print(result)

# Alternative way 
even = np.expand_dims(even_numbers,axis = 0)
odd = np.expand_dims(odd_numbers,axis = 0)
matrix = np.concatenate((even,odd), axis = 0)

print(matrix)

# Exercise 2
import numpy as np

# Create array A (3x3 with values 1-9)
A = np.arange(1, 10).reshape(3, 3)

# Create array B (3x3 with values 9-1)
B = np.arange(9, 0, -1).reshape(3, 3)

print("Array A:")
print(A)
print("\nArray B:")
print(B)

# 1. Add A and B element-wise
print("\nA + B:")
print(A + B)

# 2. Subtract B from A element-wise
print("\nA - B:")
print(A - B)

# 3. Multiply A and B element-wise
print("\nA * B:")
print(A * B)

# 4. Divide A by B element-wise
print("\nA / B:")
print(A / B)

# Array operations on A
print("\nFirst row of A:")
print(A[0])

print("\nLast column of A:")
print(A[:, -1])

print("\nLast two rows and first two columns of A:")
print(A[1:, :2])

# Create a copy of A to modify
A_modified = A.copy()
A_modified[1] = 0
print("\nA with second row set to 0:")
print(A_modified)


# Exercise 3

import igl
import polyscope as ps
V, F = igl.read_triangle_mesh("./cow/processed_mesh.obj")
print(type(V),type(F), V.shape,F.shape)


face_id = 6
vertex_id = F[face_id,:]
V_triangle = V[vertex_id]
# Initialize polyscope
ps.init()

# Register the mesh with polyscope
ps.register_point_cloud("cow",V)
ps.register_surface_mesh("mesh", V_triangle, np.array([[0,1,2]]))

# Show the visualization
ps.show()