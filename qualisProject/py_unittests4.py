# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 19:40:16 2019

@author: jith_
Nose TestCases
"""

import unittest
import math
from proj.circle import Circle
from nose.tools import assert_raises
from nose.tools import assert_equals

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

class TestCircleCreation:

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # the value of c1.radius equal to 2.5 or not
        c1=Circle(2.5)      
        assert_equals(c1.radius,2.5)

    def test_creating_circle_with_negative_radius(self):
        # Try Defining a circle 'c' with radius -2.5 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"
        with assert_raises(ValueError):
            c=Circle(-2.5)

    def test_creating_circle_with_greaterthan_radius(self):
        # Try Defining a circle 'c' with radius 1000.1 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"       
        with assert_raises(ValueError):
            c=Circle(1000.1)

    def test_creating_circle_with_nonnumeric_radius(self):
        # Try Defining a circle 'c' with radius 'hello' and see 
        # if it raises a TypeError with the message
        # "radius must be a number"    
        with assert_raises(TypeError):
            c=Circle('hello')
        

class TestCircleArea:
    def	 test_circlearea_with_random_numeric_radius(self):
		# creates a circle 'c1' with radius 2.5 
		# check if it's computed area matches the value 19.63
        c1=Circle(2.5)      
        assert_equals(c1.area(),19.63)
		
	def test_circlearea_with_min_radius(self):
		# creates a circle 'c2' with radius 0 and 
		# check if it's computed area matches the value 0
        c2=Circle(0)      
        assert_equals(c2.area(),0)
		
	def test_circlearea_with_max_radius(self):
		# creates a circle 'c3' with radius 1000 
		# check if it's computed area matches the value 3141592.65
        c3=Circle(1000)      
        assert_equals(c3.area(),3141592.65)	
		
class TestCircleCircumference:
    def	 test_circlecircum_with_random_numeric_radius(self):
		# creates a circle 'c1' with radius 2.5 
		# check if it's computed area matches the value 15.71
        c1=Circle(2.5)      
        assert_equals(c1.circumference(),15.71)
		
	def test_circlecircum_with_min_radius(self):
		# creates a circle 'c2' with radius 0 and 
		# check if it's computed circumference matches the value 0
        c2=Circle(0)      
        assert_equals(c2.circumference(),0)
		
	def test_circlecircum_with_max_radius(self):
		# creates a circle 'c3' with radius 1000 
		# check if it's computed circumference matches the value 6283.19
        c3=Circle(1000)      
        assert_equals(c3.circumference(),6283.19)
		
		


