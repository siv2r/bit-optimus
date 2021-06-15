from classes.transaction import Transaction
import csv


class Mempool():
    def __init__(self, fileName):
        self.fileName = fileName
        self.txns = list()
        self.eqTxns = list()
        self.visitedTxids = set()

    def parse_csv(self):
        with open(self.fileName, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            idx = 0
            for line in csv_reader:
                newTxn = Transaction(
                    line['tx_id'], line['fee'], line['weight'], line['parents '])
                self.txns.append(newTxn)

    def createOneEqTxn(self, tx):
        # mark the tx as visited
        self.visitedTxids.add(tx.txid)

        if tx.cntParent() == 0:
            return tx
        else:
            eqTxnId, eqTxnFee, eqTxnWeight,  = '', 0, 0
            # include par
            for parTxid in tx.parents:
                # if a parent is visited don't visit
                if parTxid in self.visitedTxids:
                    continue

                parIdx = self.findTxnIndex(parTxid)
                par = self.txns[parIdx]
                parEqTxn = self.createOneEqTxn(par)
                eqTxnId = parEqTxn.txid if (
                    eqTxnId == '') else eqTxnId + '\n' + parEqTxn.txid
                eqTxnFee += parEqTxn.fee
                eqTxnWeight += parEqTxn.weight

            # include curr tx
            eqTxnId = tx.txid if (eqTxnId == '') else eqTxnId + '\n' + tx.txid
            eqTxnFee += tx.fee
            eqTxnWeight += tx.weight

            return Transaction(eqTxnId, eqTxnFee, eqTxnWeight, '')

    def createEqTxnPool(self):

        # mark visited nodes none
        self.visitedTxids = set()

        for tx in self.txns:
            # if node is visited move to next
            if tx.txid in self.visitedTxids:
                continue

            eqTxn = self.createOneEqTxn(tx)
            self.eqTxns.append(eqTxn)

        # remove all visited txns when creating equivalent transaction
        # is this neccessary?
        # for tx in self.eqTxns:
        #     if tx.txid in self.visitedTxids:
        #         self.eqTxns.remove(tx)

    def findTxnIndex(self, txid):
        for i in range(len(self.txns)):
            if self.txns[i].txid == txid:
                return i

        raise Exception(
            'transaciton id: {} not present in Mempool.txns'.format(txid))

    def findEqTxnIndex(self, txid):
        for i in range(len(self.eqTxns)):
            currEqTxnIds = self.eqTxns[i].txid.split('\n')
            if txid in currEqTxnIds:
                return i

        raise Exception(
            'transaciton id: {} not present in Mempool.txns'.format(txid))

    def print(self):
        record = 0
        for tx in self.txns:
            record += 1
            print("Record {}:".format(record))
            # print the transaction
            tx.print()
