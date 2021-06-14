from classes.transaction import Transaction
import csv


class Mempool():
    def __init__(self, fileName):
        self.fileName = fileName
        self.txns = list()
        self.idToIndex = dict()

    def parse(self):
        with open(self.fileName, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            idx = 0
            for line in csv_reader:
                newTxn = Transaction(
                    line['tx_id'], line['fee'], line['weight'], line['parents '])
                self.txns.append(newTxn)
                # dictionary maping tx_id to txns object
                self.idToIndex[newTxn.txid] = idx
                idx += 1

    def print(self):
        record = 0
        for tx in self.txns:
            record += 1
            print("Record {}:".format(record))
            # print the transaction
            tx.print()

    def findIndex(self, txid):
        return self.idToIndex[txid];
