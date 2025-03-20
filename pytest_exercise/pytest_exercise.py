
def add(a,b):
    """Correct function. Passes unit test."""
    return a+b

def add_wrong(a,b):
    """Mistake in function. Fails unit test."""
    return a-b

def fizzbuzz(n):
    """ Implementation of Fizz Buzz.
    """
    if isinstance(n,int) == False:
        raise ValueError("input must be an integer")
    if n <= 0:
        raise ValueError("zero or negative numbers are not allowed")
    
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
