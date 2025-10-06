"""
A simple calculator module providing basic and advanced arithmetic operations.

This module includes functions for addition, subtraction, multiplication,
division, exponentiation, and square roots, with built-in validation
and error handling.
"""

import math
from typing import Union

# A type alias for cleaner type hints
Numeric = Union[int, float]

def add(a: Numeric, b: Numeric) -> float:
    """Adds two numbers together."""
    return float(a + b)

def subtract(a: Numeric, b: Numeric) -> float:
    """Subtracts the second number from the first."""
    return float(a - b)

def multiply(a: Numeric, b: Numeric) -> float:
    """
    Multiplies two numbers after validating they are numeric.
    
    Raises:
        TypeError: If either input is not an integer or float.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return float(a * b)

def divide(a: Numeric, b: Numeric) -> float:
    """
    Divides the first number by the second with validation.
    
    Raises:
        TypeError: If either input is not an integer or float.
        ValueError: If the second number (divisor) is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero.")
    return float(a / b)

def power(a: Numeric, b: Numeric) -> float:
    """Raises the first number to the power of the second."""
    return float(a ** b)

def square_root(a: Numeric) -> float:
    """
    Calculates the square root of a number.
    
    Raises:
        ValueError: If the input number is negative.
    """
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

# This block demonstrates the module's usage when run as a script
if __name__ == "__main__":
    print("🧮 Calculator Module Demonstration 🧮")
    
    # --- Basic Operations ---
    print("\n--- Basic Operations ---")
    print(f"8 + 4 = {add(8, 4)}")
    print(f"8 - 4 = {subtract(8, 4)}")
    
    # --- Advanced Operations ---
    print("\n--- Advanced Operations ---")
    print(f"8 * 4 = {multiply(8, 4)}")
    print(f"8 / 4 = {divide(8, 4)}")
    print(f"2 to the power of 8 = {power(2, 8)}")
    print(f"Square root of 64 = {square_root(64)}")
    
    # --- Error Handling Demonstration ---
    print("\n--- Error Handling ---")
    try:
        print("Attempting to divide by zero...")
        divide(10, 0)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        print("Attempting square root of a negative number...")
        square_root(-9)
    except ValueError as e:
        print(f"Caught expected error: {e}")
        
    try:
        print("Attempting to multiply with a string...")
        multiply(5, "three")
    except TypeError as e:
        print(f"Caught expected error: {e}")