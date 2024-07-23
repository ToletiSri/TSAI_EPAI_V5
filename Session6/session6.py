"""TSAI - EPAi-V5 Assignment 6 - Scopes and closures"""

from functools import wraps

def doc_string_checker():
    """closure that takes a function and then check whether
    the function passed has a docstring with more than 50 characters"""
    min_char_count = 50
    def inner(fn, *args):
        fnDocString = fn.__doc__
        word_count = len(fnDocString.split())
        #print(word_count)
        return True if word_count > min_char_count else False
    return inner


def memoize_fib(fn):
    """A decorator function (closure), that memoizes the function"""
    cache = dict()
    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize_fib
def next_fibonacci(index):
    """closure that gives the next fibonacci number.
    Note that although this function is not a closure directly,
    it wraps a closure, hence making this a closure as well"""
    return 1 if index < 3 else next_fibonacci(index-1) + next_fibonacci(index-2)


def function_counter(fn):
    """This closure is a function counter,
    this can accept any function and keep count of
    how many times the function was called in a dictionary"""
    dict_counter = {}

    def inner(fn):
        fnName = fn.__name__
        if fnName not in dict_counter.keys():
            dict_counter[fnName] = 1
        else:
            dict_counter[fnName] = dict_counter[fnName] + 1
        return dict_counter[fnName]
    inner(fn)


@function_counter
def dec_factory_calculator(calc_fn):
    fnName =  calc_fn.__name__
    if fnName not in ('add','mul','div'):
            raise ValueError("accepts only functions - 'add', 'mul', 'div'")
    def add(a, b):
        return a+b
    def mul(a, b):
        return a*b
    def div(a, b):
        if b == 0:
            raise ValueError("b can't be 0, division by 0 not allowed")
        return a/b

    if fnName == "add":
        return add
    if fnName == "mul":
        return mul
    if fnName == "div":
        return div