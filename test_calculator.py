import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(5, 5) == 10
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(3, -5) == -15 
    assert multiply(6, 2) == 12
    assert multiply(10, -10) == -100
    assert multiply(0, 0) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 5) == 2
    assert divide(-4, -4) == 1
    assert divide(20, 5) == 4