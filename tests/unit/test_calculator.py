"""
Unit tests for the calculator module.

This test suite uses pytest's parametrization to efficiently test a wide
range of inputs and expected outcomes for each calculator function.
"""

import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root


class TestBasicOperations:
    """Tests for add and subtract functions."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),  # Positive numbers
            (-1, -1, -2),  # Negative numbers
            (-5, 3, -2),  # Mixed sign
            (10, 15, 25),  # Larger numbers
            (0, 0, 0),  # Zeros
        ],
    )
    def test_add(self, a, b, expected):
        """Test the add function with various inputs."""
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 3, 2),  # Positive numbers
            (-1, -1, 0),  # Negative numbers
            (-5, -3, -2),  # Mixed sign
            (10, 4, 6),  # Larger numbers
            (0, 0, 0),  # Zeros
        ],
    )
    def test_subtract(self, a, b, expected):
        """Test the subtract function with various inputs."""
        assert subtract(a, b) == expected


class TestMultiplyDivide:
    """Tests for multiply and divide functions, including validation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (3, 4, 12),  # Positive numbers
            (5, 0, 0),  # Multiply by zero
            (-2, 3, -6),  # Mixed sign
            (-4, -5, 20),  # Negative numbers
        ],
    )
    def test_multiply(self, a, b, expected):
        """Test the multiply function with various numeric inputs."""
        assert multiply(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 2, 5),  # Positive numbers
            (-10, 2, -5),  # Mixed sign
            (-12, -3, 4),  # Negative numbers
        ],
    )
    def test_divide(self, a, b, expected):
        """Test the divide function with various numeric inputs."""
        assert divide(a, b) == expected

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide 10 by zero."):
            divide(10, 0)

    @pytest.mark.parametrize("a, b", [("5", 3), (5, "3")])
    def test_multiply_with_invalid_type_raises_error(self, a, b):
        """Test that multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(a, b)

    def test_divide_with_invalid_type_raises_error(self):
        """Test that divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestAdvancedOperations:
    """Tests for power and square root functions."""

    @pytest.mark.parametrize(
        "base, exp, expected",
        [
            (2, 3, 8),  # Positive integers
            (5, 2, 25),  # Another positive
            (5, 0, 1),  # Zero exponent
            (0, 0, 1),  # Zero base and exponent
        ],
    )
    def test_power(self, base, exp, expected):
        """Test the power function with various inputs."""
        assert power(base, exp) == expected

    @pytest.mark.parametrize(
        "num, expected",
        [
            (4, 2),
            (9, 3),
            (16, 4),
            (0, 0),
        ],
    )
    def test_square_root(self, num, expected):
        """Test the square_root function with valid inputs."""
        assert square_root(num) == expected

    def test_square_root_of_negative_raises_error(self):
        """Test that square root of a negative number raises a ValueError."""
        with pytest.raises(
            ValueError, match="Cannot calculate the square root of a negative number."
        ):
            square_root(-4)
