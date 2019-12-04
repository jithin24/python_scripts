# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:11:04 2019

@author: 583435
"""

class InsufficientException(Exception):
    pass

class MobileInventory: 
    
    def __init__(self, inventory=None):
    # Define the initialization method below
        if(inventory is None or len(inventory)==0):
            self.balance_inventory={}
        else:
            if type(inventory)==dict:
                for i in inventory:
                    if(type(i)==str):
                        #print("passed")
                        pass
                    else:
                        raise ValueError("Mobile model name must be a string")
                    
                    if(type(inventory[i])==int and inventory[i]>0):
                        #print("passed")
                        pass
                    else:
                        raise ValueError("No. of mobiles must be a positive integer")
                self.balance_inventory = inventory
            else:
                raise TypeError("Input inventory must be a dictionary")
    
    def add_stock(self,new_stock):
    #adds new stock of mobiles to existing stock
        if type(new_stock)==dict:
            for ns in new_stock:
                if(type(ns)==str):
                    #print("passed")
                    pass
                else:
                    raise ValueError("Mobile model name must be a string")
                
                if(type(new_stock[ns])==int and new_stock[ns]>0):
                    #print("passed")
                    pass
                else:
                    raise ValueError("No. of mobiles must be a positive integer")
                if ns in self.balance_inventory:
                    self.balance_inventory[ns]=self.balance_inventory[ns]+new_stock[ns]
                else:
                    self.balance_inventory.update({ns : new_stock[ns]})
        else:
            raise TypeError("Input Stock must be a dictionary")
    
    def sell_stock(self,requested_stock):
    #adds new stock of mobiles to existing inventory
        if type(requested_stock)==dict:
            for rs in requested_stock:
                if(type(rs)==str):
                    #print("passed")
                    pass
                else:
                    raise ValueError("Mobile model name must be a string")
                
                if(type(requested_stock[rs])==int and requested_stock[rs]>0):
                    #print("passed")
                    pass
                else:
                    raise ValueError("No. of mobiles must be a positive integer")
                if rs in self.balance_inventory:
                        #print("found " + rs)
                        existCount=self.balance_inventory[rs]
                        if(existCount<requested_stock[rs]):
                            raise InsufficientException("Insufficient Stock")
                        else:
                            self.balance_inventory[rs]=self.balance_inventory[rs]-requested_stock[rs]
                else:
                    raise InsufficientException("No Stock. New Model Request")
        else:
            raise TypeError("Requested stock must be a dictionary")

        
try:    
    m1=MobileInventory({'iPhone Model X':100, 'Xiaomi Model Y': 1000, 'Nokia Model Z':25})
    #m1.view_stock()
    m1.add_stock({'iPhone Model X':50, 'Xiaomi Model Y': 2000, 'Nokia Model A':10})
    #m1.sell_stock({'iPhone Model X':5})
    print(m1.balance_inventory)
except ValueError as ve:
    print(str(ve))
except InsufficientException as ie:
    print(str(ie))
except Exception as e:
    print(str(e))