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
    def __init__(self):
        """Initialize the window and establish
        the data model."""
        EasyFrame.__init__(self, title = "ATM")
        self.bank = self.getBank()
        self.account = None
        # Create and add the widgets to the window.

        # Atm part for exisiting accounts
        atmPanel = self.addPanel(row = 0, column = 0)

        atmPanel.addLabel(text = "Name", row = 0, column = 0)
        atmPanel.addLabel(text = "PIN", row = 1, column = 0)
        atmPanel.addLabel(text = "Amount", row = 2, column = 0)
        atmPanel.addLabel(text = "Status", row = 3, column = 0)
        self.nameField = atmPanel.addTextField(text = "", row = 0, column = 1, width = 40)
        self.pinField = atmPanel.addTextField(text = "", row = 1, column = 1, width = 40)
        self.pinField.bind("<Return>", lambda event: self.login())
        self.amountField = atmPanel.addFloatField(value = 0.0, row = 2, column = 1, state = "disabled",
                                            width = 40)
        self.statusField = atmPanel.addTextField(text = "Enter your name and PIN to login", row = 3, column = 1,
                                            state = "readonly", width = 40)
        self.balanceButton = atmPanel.addButton(text = "Balance", row = 0, column = 2, state = "disabled",
                                            command = self.getBalance)
        self.depositButton = atmPanel.addButton(text = "Deposit", row = 1, column = 2,
                                            state = "disabled", command = self.deposit)
        self.withdrawButton = atmPanel.addButton(text = "Withdraw", row = 2, column = 2,
                                            state = "disabled", command = self.withdraw)
        self.loginButton = atmPanel.addButton(text = "Login", row = 3, column = 2,
                                        command = self.login)
        self.fastLoginButton = atmPanel.addButton(text = "Fast login", row = 4, column = 0, 
                                            columnspan = 4, command = self.fastLogin)

        # Promotion part for newcomers
        bgColor = "gray"
        accountPanel = self.addPanel(row = 1, column = 0, background = bgColor)

        accountPanel.addLabel(text = "", row = 0, column = 0, background = bgColor)
        accountPanel.addLabel(text = "Don't have an account?", row = 1, column = 0, 
                                sticky = "NSEW", background = bgColor, foreground = "white")
        accountPanel.addButton(text = "Create one!", row = 2, column = 0, command = self.createAccount)
        accountPanel.addLabel(text = "", row = 3, column = 0, background = bgColor)

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

    def createAccount(self):
        userName = self.prompterBox(title = "Create new account", promptString = "Enter your name and surname")
        if userName:
            if userName in ''.join(self.bank.accounts.keys()):
                self.messageBox(title = "Existing user", message = "Such account already exists")
            else:
                from bank import generatePIN
                from savingsaccount import SavingsAccount
                PIN = generatePIN()
                account = SavingsAccount(userName, PIN)
                self.bank.add(account)
                self.bank.save()
                message = "This is your PIN Code.\nNever show it to anybody\n\n" + PIN
                self.messageBox(title = "PIN Code", message = message)

    def getBank(self):
        fyle = self.findBankFile()
        if fyle != None:
            return Bank(fyle)
        else:
            bank = createBank(10)
            bank.save("Local__SavedBank")
            return bank

    def findBankFile(self):
        import os
        files = os.listdir(os.getcwd())
        for fyle in files:
            if "__SavedBank" in fyle:
                return fyle
        else:
            return None

def main():
    atm = ATM()
    atm.mainloop()

if __name__ == "__main__":
    main()
