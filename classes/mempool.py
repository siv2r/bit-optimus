from classes.transaction import Transaction
import csv


class Mempool():
    def __init__(self, fileName):
        self.fileName = fileName
        self.txns = list()

    def parse(self):
        with open(self.fileName, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                newTxns = Transaction(
                    line['tx_id'], line['fee'], line['weight'], line['parents '])
                self.txns.append(newTxns)

    def print(self):
        record = 0
        for tx in self.txns:
            record += 1
            print("Record {}:".format(record))
            # print the transaction
            tx.print()
