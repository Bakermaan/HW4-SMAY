from scipy.optimize import fsolve
import numpy as np
"""In this code we are trying to find the roots of two mathematical equations efficiently and determine if
there are any intersections between their solutions. Both eq1 and eq2 are defined as mathematical
functions, and the fsolve function from scipy.optimize is then used to find roots of these functions within
a specified initial range. The find_roots_efficiently function iterates over the initial range, and it uses
fsolve to find roots and ensure precision with a specified tolerance. The results are then presented
as sorted lists of unique roots for each equation. Additionally, any intersections between the sets of
roots are identified."""

# Functions as defined in prompt
def eq1(x):
    """In this function, we are defining the first equation that the roots are going to be found in.
    For our parameters, 'x' is the float variable for which the equation is defined, and it is going
    to return a value that is a result of the equation. In this function, we are importing the numpy
    cosine function that will calculate the cosine of a given angle 'x'."""
    return x - 3 * np.cos(x)

def eq2(x):
    """This function does the same thing as def eq1 does, but it just does it for the diferent formula."""
    return np.cos(2*x) - x**3

# A function to find roots efficiently
def find_roots_efficiently(func, initial_range, tolerance=1e-5):
    """In this function, we are finding the roots of a given function within a specified initial range.
    One of the parameters for this function is 'func', and it is the function where the roots are found.
    Another parameter is 'initial_range', and it is a numpy array that defines the initial range of
    values to search for roots. Our last parameter is 'tolerance', and it is a float variable that
    allows us to input the tolerance for the algorithm. It defaults to 1e-5 unless otherwise changed.
    This function then outputs a sorted list of unique roots that are found within the specified initial
    range."""
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
