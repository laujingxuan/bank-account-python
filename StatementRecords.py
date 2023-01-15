from StatementRecord import StatementRecord

class StatementRecords:
    def __init__(self):
        self.records = []

    def addRecord(self, amount, balance):
        self.records.append(StatementRecord(amount, balance))

    def printStatements(self):
        table = []
        table.append(['Date', 'Amount', 'Balance'])
        for record in self.records:
            table.append(record.retrieveStatementRecord())
        for row in table:
            print('| {:22} | {:^10} | {:^10} '.format(*row))
        