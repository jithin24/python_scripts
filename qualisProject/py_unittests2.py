# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:40:16 2019

@author: jith_
"""

import unittest
import math

# Define below the class 'Circle' and it's methods with proper doctests.
class Circle:

    def __init__(self, radius):
        # Define the initialization method below
            if not isinstance(radius, (int, float)):
                raise TypeError("radius must be a number")
            elif 1000 >=radius>=0:
                    self.radius=radius 
            else:
                raise ValueError("radius must be between 0 and 1000 inclusive")        

    def area(self):
        # Define the area functionality below
        y=math.pi*(self.radius**2)
        return round(y,2)

    def circumference(self):
        # Define the circumference functionality below
        x=math.pi*2*self.radius
        return round(x,2)

class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # the value of c1.radius equal to 2.5 or not
        c1=Circle(2.5)        
        self.assertEqual(c1.radius,2.5)

    def test_creating_circle_with_negative_radius(self):
        # Try Defining a circle 'c' with radius -2.5 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"
        with self.assertRaises(ValueError):
            c=Circle(-2.5)
            self.assertEqual(c.radius,-2.5)

    def test_creating_circle_with_greaterthan_radius(self):
        # Try Defining a circle 'c' with radius 1000.1 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"        
        with self.assertRaises(ValueError):
            c=Circle(1000.1)
            self.assertEqual(c.radius,1000.1)

    def test_creating_circle_with_nonnumeric_radius(self):
        # Try Defining a circle 'c' with radius 'hello' and see 
        # if it raises a TypeError with the message
        # "radius must be a number"       
        with self.assertRaises(TypeError):
            c=Circle('hello')
            self.assertEqual(c.radius, 'hello')
        
    
