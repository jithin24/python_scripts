# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:17:34 2018

@author: 583435
"""

"""
#Sample Doctest function
def is_anagram(a_word, b_word):
    
    >>> is_anagram("abc", "acb")
    True
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("one", "two")
    False
    
    return sorted(a_word) == sorted(b_word)
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""
    
"""
# Complete the isPalindrome function below.
def isPalindrome(x):
    # Write your doctests below.
    
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
        raise ValueError('x must be a positive integer')
    ValueError: x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
        raise TypeError('x must be an integer')
    TypeError: x must be an integer
    
    
    # Write the functionality below
    org_str = str(x)
    rev_str = reversed(org_str)
    if list(org_str) == list(rev_str):
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""    

import doctest

# Define below the class 'Circle' and it's methods with proper doctests.
class Circle:
    
    def __init__(self, radius):
        #Define the doctests for __init__ method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5
        """
        self.radius = radius
        
    def area(self):
        # Define the doctests for area method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.area()
        19.63
        """
        #Define the area functionality below
        from math import pi
        return round(pi * self.radius **2, 2)
        
        
    def circumference(self):
        # Define the doctests for circumference method below
        """
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define the circumference functionality below
        from math import pi
        return round(2* pi * self.radius, 2)

if __name__ == '__main__':
    doctest.testmod()