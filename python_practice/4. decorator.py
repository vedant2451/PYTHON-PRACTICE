# A simple decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something before the function runs.")
#         func()
#         print("Something after the function runs.")

#     return wrapper


# Using the decorator
# @my_decorator
# def say_hello():
#     print("Hello!")

# @my_decorator
# def neel():
#     print("hello i am neel")


# # # Call the decorated function
# say_hello()

# neel()

# new code


import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        total_time = end_time - start_time  # Calculate the time taken
        print(f"Time taken by {func.__name__}: {total_time:.6f} seconds \n")

    return wrapper


@timeit
def example_function(a, b):
    """this is the doc string in side the function"""
    print(a + b)
    for i in range(1000000000):
        pass


example_function(5, 6)


# print(example_function.__doc__)
# print(example_function.__name__)
