""" File: main.py
    Source: ...
    Date: 05 / 10 / 2018
    Author: Pavel Paranin""" 

from atm import ATM
from breezypythongui import EasyFrame

class CreateAccount(EasyFrame):
    """Wizard to create an account in a bank simulator"""

    def __init__(self):
        EasyFrame.__init__(self, title = "Welcome in our bank!")
        