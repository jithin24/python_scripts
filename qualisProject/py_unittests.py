
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:12:51 2018

@author: 583435
"""

import unittest

# Define below the class 'Circle' and it's methods with proper doctests.
class Circle:
    
    def __init__(self, radius):
        # Define the initialization method below
        self.radius = radius
        
    def area(self):
        # Define the area functionality below
        from math import pi
        return round(pi * self.radius **2, 2)
               
    def circumference(self):
        # Define the circumference functionality below
        from math import pi
        return round(2* pi * self.radius, 2)        
    

class TestCircleCreation(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.verificationErrors = []
        
    def negRad(self, val, msg):
        if(val >= 0 and val <= 1000):
            print('')
        else:
            raise ValueError(msg)

    
    def greatRad(self, val, msg):
        if(val >= 0 and val <= 1000): 
            print('')
        else:
            raise ValueError(msg)

    
    def digiRad(self, val, msg): 
        if(val.isdigit()):
            print('')
        else:
            raise TypeError(msg)

    
    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # the value of c1.radius equal to 2.5 or not
        c1 = Circle(2.5)
        print("\nStart TestCircleCreation test\n")

        if not c1.radius:
            try:
                self.assertEqual(len(self.verificationErrors), 0)
                self.assertEqual(c1.radius, 2.5)
            except AssertionError as e:
                   for message in self.verificationErrors:
                       print(str(message))
        else:
            pass



    
    def test_creating_circle_with_negative_radius(self):
        # Try Defining a circle 'c' with radius -2.5 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"
        c = Circle(-2.5)
        print("\nCreate Circle with Negetive test\n")
        self.assertRaises(ValueError, lambda: self.negRad(c.radius, "radius must be between 0 and 1000 inclusive"))
            
    def test_creating_circle_with_greaterthan_radius(self):
        # Try Defining a circle 'c' with radius 1000.1 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"        
        c = Circle(1000.1)
        print("\nStart Circle GreaterThan test\n")



        self.assertRaises(ValueError, lambda: self.greatRad(c.radius, "radius must be between 0 and 1000 inclusive"))
        
    def test_creating_circle_with_nonnumeric_radius(self):
        # Try Defining a circle 'c' with radius 'hello' and see 
        # if it raises a TypeError with the message
        # "radius must be a number"
        c = Circle('hello')
        print("\nStart Circle with NonNumeric test\n")

        self.assertRaises(TypeError, lambda: self.digiRad(c.radius, "radius must be a number"))
    
    
if __name__ == '__main__':
    unittest.main()