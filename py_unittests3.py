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
                #self.radius=radius

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
        self.assertEqual(c1.area(),19.63)

    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0 and check if 
        # it's area is 0
        c2=Circle(0) 
        self.assertEqual(c2.area(),0)
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1 and check if 
        # it's area is 3141592.65
        self.assertRaises(ValueError, Circle, 1000.1) 
        c3=Circle(1000.1)
        self.assertEqual(c3.area(),3141592.65)
    
