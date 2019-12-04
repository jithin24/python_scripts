# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:28:07 2019

@author: 583435
"""

class Account():
    def __init__(self, owner, balance=0):
        self.min_balance = 1000
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        '''
        This function allows User to  deposit an Amount to his account
        '''
        chk_deposit=False
        if(int(amount)>0):
            self.balance += int(amount)
            chk_deposit=True
        else:
            pass
            print(f"Error! Invalid Deposit Amount {amount}")
        return chk_deposit
    
    def withdrawal(self, amount):
        '''
        Function allows user to withdraw an Amount from Account
        Check is performed for minimum Balance and fund balance 
        before allowing the Transaction
        '''
        check_withdraw=False
        if(int(amount)>self.balance):
            print("Sorry! Insuffecient balance..." , self.balance)
        elif(self.balance-int(amount)<self.min_balance):
            self.balance -= int(amount)
            print("Warning! Balance amount is below min balance ", self.balance)
        else:
            self.balance -= int(amount)
            check_withdraw=True
            print("Success! Balance amount ", self.balance)
        return check_withdraw
    
    def check_balance(self):
        '''
        Function allows the User to verify present balance
        '''
        print("Current Balance: " , self.balance)
    
    def __str__(self):
        return f"Account Owner: {self.owner} \nAvailable Balance {self.balance}"