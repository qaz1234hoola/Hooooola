"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract , multiply

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def multiply(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a * b


    def divide(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Division requires numeric inputs")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


# TODO: Students will add TestMultiplyDivide class

    def test_add_negative_numbers(self):
    # """Test adding negative numbers""" 
        assert add(-1, -1) == -2 
        assert add(-5, 3) == -2

    def test_subtract_negative_numbers(self): 
    # """Test subtracting negative numbers""" 
        assert subtract(-1, -1) == 0 
        assert subtract(-5, -3) == -2


class TestMultiplyDivide:
#  """Test multiplication and division operations"""
    def test_multiply_positive_numbers(self):
#  """Test multiplying positive numbers"""
        assert multiply(3, 4) == 12 
        assert multiply(7, 8) == 56 
 
    def test_multiply_by_zero(self): 
#  """Test multiplying by zero""" 
        assert multiply(5, 0) == 0 
        assert multiply(0, 10) == 0 
 
    def test_multiply_negative_numbers(self): 
#  """Test multiplying negative numbers""" 
        assert multiply(-2, 3) == -6 
        assert multiply(-4, -5) == 20 
 
    def test_divide_positive_numbers(self): 
#  """Test dividing positive numbers""" 
        assert divide(10, 2) == 5 
        assert divide(15, 3) == 5 
 
    def test_divide_negative_numbers(self): 
#  """Test dividing negative numbers""" 
        assert divide(-10, 2) == -5 
        assert divide(-12, -3) == 4   