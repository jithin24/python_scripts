# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:13:04 2019

@author: 583435
"""

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from proj.inventory import MobileInventory,InsufficientException
import pytest 

class TestingInventoryCreation:
    
    def test_creating_empty_inventory(self):
        m1=MobileInventory({})
        assert m1.balance_inventory=={}
        
    def test_creating_specified_inventory(self):
        m1=MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
        assert m1.balance_inventory=={'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25}

    def test_creating_inventory_with_list(self):
        with pytest.raises(TypeError, message="Input inventory must be a dictionary"):
            MobileInventory(['iPhone Model X', 'Xiaomi Model Y', 'Nokia Model Z'])
    
    def test_creating_inventory_with_numeric_keys(self):
        with pytest.raises(ValueError, message="Mobile model name must be a string"):
            MobileInventory({1:'iPhone Model X', 2:'Xiaomi Model Y', 3:'Nokia Model Z'})
    
    def test_creating_inventory_with_nonnumeric_values(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            MobileInventory({'iPhone Model X':'100', 'Xiaomi Model Y': '1000', 'Nokia Model Z':'25'})
        
    def test_creating_inventory_with_negative_value(self):
        with pytest.raises(ValueError, message="No. of mobiles must be a positive integer"):
            MobileInventory({'iPhone Model X':-45, 'Xiaomi Model Y': 200, 'Nokia Model Z':25})