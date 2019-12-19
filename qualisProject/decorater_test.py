# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:04:06 2019

@author: 583435
"""

"""
#First Sample Function
def decorator(func):
    def inner_function(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)
    return inner_function


@decorator
def foobar(x):
    return x**2

print(foobar(3))
"""


def star(func): 
    def inner(*args, **kwargs): 
        print("*" * 3) 
        func(*args, **kwargs) 
        print("*" * 3) 
    return inner

def percent(func): 
    def inner(*args, **kwargs): 
        print("%" * 3) 
        func(*args, **kwargs) 
        print("%" * 3) 
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("Hello")



"""
def smart_divide(func): 
    def wrapper(*args): 
        a, b = args 
        if b == 0: 
            print('oops! cannot divide') 
            return
        return func(*args)
    return wrapper

@smart_divide 
def divide(a, b): 
    return a / b

#print(divide.name) 
print(divide(4, 16))
print(divide(8,0))
"""

"""
#Trial function
def decorate_X(func):
    print("decorate X Trigger")
    def wrapper_func():
        print("X Wrapper Trigger")
        print("X=X"*10)
        func()
        print("X=X"*10)
    return wrapper_func

def decorate_Y(func):
    print("decorate Y Trigger")
    def wrapper_func():
        print("Y Wrapper Trigger")
        print("Y=Y"*10)
        func()
        print("Y=Y"*10)
    return wrapper_func

@decorate_Y
@decorate_X
def greeting():
    print("Hello from Python")

greeting()
"""