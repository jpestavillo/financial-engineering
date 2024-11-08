# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:34:49 2020

@author: Estavillo
"""
#A
import functools



def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return ' '.join(reversed(func(*args, **kwargs)))  if type(func(*args, **kwargs))==str else None
    return wrapper 

# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
    return 1957

# TEST OUPUT
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)
#%%
# MODIFY THIS DECORATOR
from typing import List
def prime_filter(func):
    """Given a list of integers, return only the prime integers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return [isPrime(x) for x in func(*args, *kwargs)]
    return wrapper

def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return None
        else:
            return x
# TARGET FUNCTIONS
@prime_filter
def numbers(from_num: int, to_num: int) -> List[int]:
    return [num for num in range(from_num, to_num)]

# TEST OUPUT
print(numbers(from_num=2, to_num=20))
#%% C
# MODIFY THIS DECORATOR
from typing import List
def choose_one(func):
    """Given a list of elements, select a random one."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return random.choice(func(*args, **kwargs))
    return wrapper

# TARGET FUNCTIONS
@choose_one
def available_options() -> List[str]:
    return ["A", "B", "C"]

# TEST OUPUT
print(available_options())

#%%
#D
# MODIFY THIS META DECORATOR
import random
def power(n: int):
    """Given a number, return a tuple where the first element is the
    original number and the second is the nth power."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return (func(*args, **kwargs),n)
        return wrapper
    return decorator

# TARGET FUNCTIONS
@power(n=5)
def get_random_number(from_num: int, to_num: int):
    return random.randint(a=from_num, b=to_num)

# TEST OUPUT
print(get_random_number(50, 100))
#%%
# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# TEST OUPUT
print(
    get_user(name="Alice", age=30),
    get_user(name="Bob", age=25),
    sep="\n"
)
#%%
# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return  ["*"*(len(func(*args, **kwargs)))]
        return wrapper
    return decorator

# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# TEST OUPUT
print(
    get_user(name="Alice", age=30),
    get_user(name="Bob", age=25),
    sep="\n"
)