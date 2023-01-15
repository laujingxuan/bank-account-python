from StatementRecords import StatementRecords

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.records = StatementRecords()

    def withdraw(self, amount):
        if amount <= 0 or self.balance > amount:
            return False
        self.balance -= amount
        self.records.addRecord(-amount, self.balance)
        return True
    
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        self.records.addRecord(amount, self.balance)
        return True

    def printStatement(self):
        self.records.printStatements()
