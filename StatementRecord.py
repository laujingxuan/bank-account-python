from datetime import datetime


class StatementRecord:
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        now = datetime.now()
        timeString = now.strftime("%W %b %Y %I:%M:%S%p")
        self.time = timeString

    def retrieveStatementRecord(self):
        return [self.time, self.amount, self.balance]