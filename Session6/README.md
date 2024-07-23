[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gQ_doPhb)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15280477&assignment_repo_type=AssignmentRepo)
# EPAi 5 Session 6 Scopes and closures

## Session 6 Topics

Global and Local Scopes \
Non Local Scopes \
Closures \

This assigment consists of the implementation of following fuctions: 

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200 \
2. Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100 \
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250 \
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250

"""TSAI - EPAi-V5 Assignment 6 - Scopes and closures"""

from functools import wraps
#### doc_string_checker
def doc_string_checker(fn, *args):
    """closure that takes a function and then check whether 
       the function passed has a docstring with more than 50 characters"""
    min_char_count = 50
    def inner(fn):
        fnDocString = fn.__doc__
        word_count = fnDocString.split()
        return True if word_count > 50 else False
    inner()


def memoize_fib(fn):
    """A decorator function (closure), that memoizes the function"""
    cache = dict()    
    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]    
    return inner

#### next_fibonacci
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
    inner()

#### dec_factory_calculator   
@function_counter
def dec_factory_calculator(fn): 
    fnName =  fn.__name__  
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
    
    if fn.__name__ == "add":
        return add
    if fn.__name__ == "mul":
        return mul
    if fn.__name__ == "div":
        return div
