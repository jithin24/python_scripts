# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:00:05 2019

@author: 583435
"""

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from proj.inventory import MobileInventory,InsufficientException
import pytest

class TestInventoryAddStock:
    
    def setup_class(self):
        self.inventory=MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        
    def test_add_new_stock_as_dict(self):
        self.inventory.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
        assert self.inventory.balance_inventory=={'iPhone Model X':150, 'Xiaomi Model Y': 3000, 'Nokia Model Z':25, 'Nokia Model A':10}
        
    def test_add_new_stock_as_list(self):
        with pytest.raises(TypeError, message="Input inventory must be a dictionary"):
            self.inventory.add_stock(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
    
    def test_add_new_stock_with_numeric_keys(self):
        with pytest.raises(ValueError, message="Mobile model name must be a string"):
            self.inventory.add_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
    
    def test_add_new_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            self.inventory.add_stock({'iPhone Model A':'50', 'Xiaomi Model B':'2000', 'Nokia Model C':'25'})
    
    def test_add_new_stock_with_float_values(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            self.inventory.add_stock({'iPhone Model A':50.5, 'Xiaomi Model B':2000.3, 'Nokia Model C':25})
            
            
class TestInventorySellStock:

    def setup_class(self):
        self.inventory=MobileInventory({'iPhone Model A':50, 'Xiaomi Model B': 2000, 'Nokia Model C':10, 'Sony Model D':1})
        
    def test_sell_stock_as_dict(self):
        self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':20, 'Sony Model D':1})
        assert self.inventory.balance_inventory=={'iPhone Model A':48, 'Xiaomi Model B': 1980, 'Nokia Model C':10, 'Sony Model D':0}
        
    def test_sell_stock_as_list(self):
        with pytest.raises(TypeError, message="Requested stock must be a dictionary"):
            self.inventory.sell_stock(['iPhone Model A', 'Xiaomi Model B', 'Nokia Model C'])
            
    def test_sell_stock_with_numeric_keys(self):
        with pytest.raises(ValueError, message="Mobile model name must be a string"):
            self.inventory.sell_stock({1:'iPhone Model A', 2:'Xiaomi Model B', 3:'Nokia Model C'})
            
    def test_sell_stock_with_nonnumeric_values(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            self.inventory.sell_stock({'iPhone Model A':'2', 'Xiaomi Model B':'3', 'Nokia Model C':'4'})
            
    def test_sell_stock_with_float_values(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            self.inventory.sell_stock({'iPhone Model A':2.5, 'Xiaomi Model B':3.1, 'Nokia Model C':4})
    
    def test_sell_stock_of_nonexisting_model(self):
        with pytest.raises(InsufficientException, message="No Stock. New Model Request"):
            self.inventory.sell_stock({'iPhone Model B':2, 'Xiaomi Model B':5})        
    
    def test_sell_stock_of_insufficient_stock(self):
        with pytest.raises(InsufficientException, message="Insufficient Stock"):
            self.inventory.sell_stock({'iPhone Model A':2, 'Xiaomi Model B':5, 'Nokia Model C': 15})