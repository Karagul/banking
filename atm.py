""" File: atm.py
    Source: Ken Lambert - Fundamentals of Python 2018
    Date: 05 / 10 / 2018
    Author: Pavel Paranin""" 

from breezypythongui import EasyFrame
from bank import Bank, createBank

class ATM(EasyFrame):
    """Represents an ATM window.
    The window tracks the bank and the current account.
    The current account is None at startup and logout.
    """

    def __init__(self, bank):
        """Initialize the window and establish
        the data model."""
        EasyFrame.__init__(self, title = "ATM")
        self.bank = bank
        self.account = None
        # Create and add the widgets to the window.
        self.addLabel(text = "Name", row = 0, column = 0)
        self.addLabel(text = "PIN", row = 1, column = 0)
        self.addLabel(text = "Amount", row = 2, column = 0)
        self.addLabel(text = "Status", row = 3, column = 0)
        self.nameField = self.addTextField(text = "", row = 0, column = 1, width = 40)
        self.pinField = self.addTextField(text = "", row = 1, column = 1, width = 40)
        self.pinField.bind("<Return>", lambda event: self.login())
        self.amountField = self.addFloatField(value = 0.0, row = 2, column = 1, state = "disabled",
                                            width = 40)
        self.statusField = self.addTextField(text = "Enter your name and PIN to login", row = 3, column = 1,
                                            state = "readonly", width = 40)
        self.balanceButton = self.addButton(text = "Balance", row = 0, column = 2, state = "disabled",
                                            command = self.getBalance)
        self.depositButton = self.addButton(text = "Deposit", row = 1, column = 2,
                                            state = "disabled", command = self.deposit)
        self.withdrawButton = self.addButton(text = "Withdraw", row = 2, column = 2,
                                            state = "disabled", command = self.withdraw)
        self.loginButton = self.addButton(text = "Login", row = 3, column = 2,
                                        command = self.login)
        self.fastLoginButton = self.addButton(text = "Fast login", row = 4, column = 0, 
                                            columnspan = 4, command = self.fastLogin)
    
    def fastLogin(self):
        # Only for testing
        self.nameField.setText("Account 1")
        pin = ""
        for key in list(self.bank.accounts.keys()):
            key = key.split("/")
            if key[0] == "Account 1":
                pin = key[1]
        self.pinField.setText(pin)
        self.login()

    def deposit(self):
        amount = float(self.amountField.getValue())
        if amount == 0.0:
            self.statusField.setText("You didn't type in any number")
        elif amount < 0:
            self.statusField.setText("Amount should be a positive number")
        else:
            self.account.deposit(amount)
            self.statusField.setText("Deposit is succesful!")

    def getBalance(self):
        balance = self.account.balance
        self.statusField.setText("Your available balance is " + str(balance))

    def withdraw(self):
        amount = float(self.amountField.getValue())
        if amount == 0.0:
            self.statusField.setText("You didn't type in any number")
        elif amount < 0:
            self.statusField.setText("Amount should be a positive number")
        else:
            message = self.account.withdraw(amount)
            self.statusField.setText(message)

    def login(self):
        """Attempts to login the customer. If successful,
        enables the buttons, including logout."""
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.bank.get(name, pin):
            self.statusField.setText("Welcome back " + self.account.name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.loginButton["text"] = "Logout"
            self.loginButton["command"] = self.logout
            self.amountField["state"] = "normal"
        else:
            self.statusField.setText("Incorrect name or PIN. Try once again")

    def logout(self):
        self.account = None
        self.nameField.setText("")
        self.pinField.setText("")
        self.amountField.setNumber(0.0)
        self.statusField.setText("Welcome to the Bank!")
        self.balanceButton["state"] = "disabled"
        self.depositButton["state"] = "disabled"
        self.withdrawButton["state"] = "disabled"
        self.loginButton["text"] = "Login"
        self.loginButton["command"] = self.login


def main():
    bank = createBank(5)
    print(bank)
    atm = ATM(bank)
    atm.mainloop()

if __name__ == "__main__":
    main()
