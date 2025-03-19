import pytest

def add(a,b):
    """Correct function. Passes unit test."""
    return a+b

def add_wrong(a,b):
    """Mistake in function. Fails unit test."""
    return a-b

""" assert: test if expected result is actual result
    pytest expects test functions to start with "test_"
"""

def test_add():
    assert add(2,3) == 5
    assert add("space","ship") == "spaceship"
    # assert add_wrong(2,3) == 5 # as expected, this test fails.



""" Test-Driven Development: write test first, then write function to pass test.
"""

def fizzbuzz(n):
    """ Implementation of Fizz Buzz.
    """
    if isinstance(n,int) == False:
        raise ValueError("input must be an integer")
    if n<= 0:
        raise ValueError("zero or negative numbers are not allowed")
    
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzzz" # misspelled on purpose: all test should pass except one



def test_fizzbuzz_int():
    with pytest.raises(ValueError):
        fizzbuzz(2.5)
        fizzbuzz("meepmorp")

def test_fizzbuzz_zero():
    with pytest.raises(ValueError):
        fizzbuzz(0)

def test_fizzbuzz_negative():
    with pytest.raises(ValueError):
        fizzbuzz(-3)

def test_fizzbuzz_fizz():
    assert fizzbuzz(3)  == "Fizz"
    assert fizzbuzz(9)  == "Fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5)  == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(60) == "FizzBuzz"
