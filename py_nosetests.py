# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:14:31 2019

@author: jith_
"""


def test_sample_nosetest():
    assert 'HELLO' == 'hello'.upper()
    
from nose.tools import ok_, eq_
def test_using_ok():
    ok_(2+3==5)

def test_using_eq():
    eq_(2+3, 5)