# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:56:45 2019

@author: 583435
"""

import math_calc

def test_add():
    assert math_calc.add(7,3)==10
    
def test_product():
    assert math_calc.product(4,5)==20

def test_type():
    result1=math_calc.product(5,10)
    assert type(result1/10.0) is float
    
def test_multiply_strings():
    result2=math_calc.product('Hello Python', 5)
    assert 'Hello PythonHello Python' in result2