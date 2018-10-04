""" File: bank.py
    Source: Ken Lambert - Fundamentals of Python 2018
    Date: 03 / 10 / 2018
    Author: Pavel Paranin""" 

from savingsaccount import SavingsAccount

class Bank(object):

    def __init__(self):
        self.accounts = {}

    def makeKey(self, name, pin):
        """Makes and returns a key from name and pin."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an account with name and pin as a key."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes an account with name and pin as a key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns an account with name and pin as a key
        or None if not found."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes interest for each account and
        returns the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def __str__(self):
        """Return the string rep of the entire bank."""
        return '\n'.join(map(str, self.accounts.values()))

    import pickle

    def save(self, fileName = None):
        """Saves pickled accounts to a file. The parameter
        allows the user to change filenames."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self. fileName, "wb")
        for account in self.accounts.values():
            account.dump()
        fileObj.close()


    