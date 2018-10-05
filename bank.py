""" File: bank.py
    Source: Ken Lambert - Fundamentals of Python 2018
    Date: 03 / 10 / 2018
    Author: Pavel Paranin""" 

from savingsaccount import SavingsAccount
import pickle

class Bank(object):

    def __init__(self, fileName = None):
        """Creates a new dictionary to hold the accounts.
        If a filename is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break

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

    def save(self, fileName = None):
        """Saves pickled accounts to a file. The parameter
        allows the user to change filenames."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

def createBank(number = None):
    import random
    bank = Bank()
    if number > 0:
        for i in range(number):
            bank.add(SavingsAccount("Account " + str(i), 
                    ''.join([str(random.randint(1, 9)) for _ in range(4)]),
                    balance = random.randint(1, 10) * 1000))
        return bank
    else:
        return None


    