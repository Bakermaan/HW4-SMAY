from scipy.optimize import fsolve
import numpy as np

# Functions as defined in prompt
def eq1(x):
    return x**3 - 3 * np.cos(x)

def eq2(x):
    return np.cos(2*x) - x**3

# A function to find roots efficiently
def find_roots_efficiently(func, initial_range, tolerance=1e-5):
    roots = set()
    for start in initial_range:
        root, info, ier, _ = fsolve(func, start, full_output=True)
        if ier == 1:  # Root was found
            rounded_root = np.round(root[0], decimals=int(-np.log10(tolerance)))
            roots.add(rounded_root)
    return sorted(roots)

# Define initial ranges based on the expected behavior of the functions
initial_range = np.linspace(-2, 2, 400)  # A denser range might help in finding roots

# Finding roots for both equations
roots_eq1 = find_roots_efficiently(eq1, initial_range)
roots_eq2 = find_roots_efficiently(eq2, initial_range)

# Check for intersections
intersections = set(roots_eq1).intersection(roots_eq2)

print(f"Roots of eq1: {roots_eq1}")
print(f"Roots of eq2: {roots_eq2}")
if intersections:
    print(f"Intersections: {intersections}")
else:
    print("NO INTERSECTIONS")
