# # M2 - W5 | PROJECT: Presenting Data to Different Teams
# Student: Loai Siwas

# # Exercise 1
# Create your own decoratorFor this exercise, you will create your own decorator  to measure the execution time of a function. You need to do that from scratch and not use any other built-in decorators (but you are allowed to use the time() module).

# Importing the necessary packages
import time
from typing import Callable, Any

# Implementing the decorator
def measure_time(func: Callable) -> Callable:
    """
    Decorator function to measure the execution time of a function.
    :param func: The function to measure the execution time of.
    :return: The decorated function.
    """
    
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Executed {func.__name__} in {end_time - start_time} seconds.')
        return result
    
    return wrapper



# Example function to demonstrate the use of the measure_time decorator
@measure_time
def my_function():
    """
    Example function to demonstrate the use of the measure_time decorator.
    """
    x = 0
    for i in range(20000000):
        x += i
    print(x)


# calling the test function
my_function()

 
# # End of Assignment
# Student Name: Loai Siwas
