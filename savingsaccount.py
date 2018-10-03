""" File: savingaccounts.py
    Source: Ken Lambert - Fundamentals of Python 2018
    Author: Pavel Paranin"""

class SavingsAccount(object):
    """This class represents a savings account
    with the owner's name, PIN, and balance."""
    
    RATE = 0.02

    def __ini__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def getBalance(self):
        """ Returns the balance"""
        return self.balance
    
    def getName(self):
        """ Returns the name"""
        return self.name

    def getPin(self):
        """ Returns the pincode"""
        return self.pin

    def deposit(self, amount):
        """Deposits the given amount and returns None"""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraw the fiven amount"""
        if amount < 0:
            return "The amount must be >= 0"
        else:
            pass

