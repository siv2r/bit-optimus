from classes.transaction import Transaction
from classes.mempool import Mempool

class Block():
    def __init__(self, maxWeight = float('inf')):
        self.txns = []
        self.weight = 0
        self.fee = 0
        self.visitedEqTxnIds = set()
        self.maxWeight = maxWeight

    def addEqTxn(self, eqTxn, mempool):
        # mark the eqTxn as visited
        self.visitedEqTxnIds.add(eqTxn.txid)


        eqTxnIds = eqTxn.txid.split('\n')

        # # mark Txns in current EqTxns as visited
        # for txid in eqTxnIds:
        #     if txid in self.visitedTxnIds:
        #         raise Exception('Some logic error in addEqTxn')
        #     self.visitedTxnIds.add(txid)
        for txid in eqTxnIds:
            # get the txn from it's id
            txnIdx = mempool.findTxnIndex(txid)
            tx = mempool.txns[txnIdx]

            for parTxid in tx.parents:
                parEqTxnIdx = mempool.findEqTxnIndex(parTxid)
                parEqTxn = mempool.eqTxns[parEqTxnIdx]
                if parEqTxn.txid in self.visitedEqTxnIds:
                    continue
                self.addEqTxn(parEqTxn, mempool)

        # add current eqTxn
        self.txns.append(eqTxn)
        self.weight += eqTxn.weight
        self.fee += eqTxn.fee

    def selectOptEqTxns(self, mempool):
        # mark all ids as not visited
        self.visitedTxnIds = set()

        for eqTxn in mempool.eqTxns:
            if eqTxn.txid in self.visitedEqTxnIds:
                continue

            if eqTxn.weight + self.weight <= self.maxWeight:
                self.addEqTxn(eqTxn, mempool)

    def print(self):
        print("transactions: {}".format(self.txns))
        print("fee: {}".format(self.fee))
        print("weight: {}\n".format(self.weight))


    def createTxt(self):
        with open('block.txt', 'w') as file_handle:
            for tx in self.txns:
                file_handle.write('{}\n'.format(tx.txid))
