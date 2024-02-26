import numpy as np
from scipy.linalg import solve

"""In this code, we are solving a linear system of equations Ax=b using scipy's solve function. We first
define the 3x3 coefficient matrix as A1, and the 4x4 coefficient matrix as A2, and we are using a numpy
array to define them in our parameters. We then define the constant matrices as b1 and b2, and we once again
use a numpy array to do so. After defining our matrices, we use the solve function in scipy to simultaneously
solve our two matrices, and we are left with two numpy arrays for our solution vector x."""
# Define the coefficient matrices
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])

A2 = np.array([[1, -10, 2, 4],
               [3, 1, 4, 12],
               [9, 2, 3, 4],
               [-1, 2, 7, 3]])

# Define the constant matrices
b1 = np.array([2, 12, 10])
b2 = np.array([2, 12, 21, 37])

# Solve the first matrix
x1 = solve(A1, b1)

# Solve the second matrix
x2 = solve(A2, b2)

# Print the solutions
print("Solution to the first matrix:")
print(x1)
print("\nSolution to the second matrix:")
print(x2)
