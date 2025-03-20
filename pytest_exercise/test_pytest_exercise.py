import pytest
from pytest_exercise import *

""" assert: test if expected result is actual result
    pytest expects test functions to start with "test_"
"""

def test_add():
    assert add(2,3) == 5
    assert add("space","ship") == "spaceship"
    # assert add_wrong(2,3) == 5 # as expected, this test fails.



""" Test-Driven Development: write test first, then write function to pass test.
"""

def test_fizzbuzz_int():
    with pytest.raises(ValueError):
        fizzbuzz(2.5)
        fizzbuzz("spaceship")

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

def test_fizzbuzz_misc():
    assert fizzbuzz(4) == 4
    assert fizzbuzz(7) == 7
