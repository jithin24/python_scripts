# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:54:10 2019

@author: jith_
"""

import unittest

def pow2num(x, y):
    """Returns x power of y.
    >>> pow2num(2, 6)
    64
    >>> pow2num(10, -3)
    0.001
    """
    return x**y

def add2num(x, y):
    """Returns x addition y.
    >>> add2num(2, 6)
    8
    >>> add2num(10, -3)
    7
    """
    return x+y

class Testadd2num(unittest.TestCase):
    def setUp(self):
        print('Executed before start of every test')
        
    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)

    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)

    def tearDown(self):
        print('Executed at the end of every test')
        

class Testpow2num(unittest.TestCase):
    def setUp(self):
        print('Executed before start of every test')
        
    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -27)
    
    def tearDown(self):
        print('Executed at the end of every test')    
        
#if __name__ == '__main__':
#    unittest.main()
    