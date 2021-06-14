from classes.transaction import Transaction
from classes.mempool import Mempool

class Block():
    def __init__(self):
        self.txns = []
        self.weight = 0
        self.fee = 0
        self.visited = set()
    
    def _addCurrTxn(self, tx):
        self.txns.append(tx)
        self.weight += tx.weight
        self.fee += tx.fee
        self.visited.add(tx.txid)


    def add(self, tx, mempool):
        if tx.cntParent() == 0:
            self._addCurrTxn(tx)
        else:
            # add all the parents
            for parTxid in tx.parents:
                if parTxid in self.visited:
                    continue
                
                parIdx = mempool.findIndex(parTxid)
                par = mempool.txns[parIdx]
                self.add(par, mempool)

            # now add the child
            self._addCurrTxn(tx)

    def isValid(self):
        visitedTxnId = set()

        for tx in self.txns:
            visitedTxnId.add(tx.txid)
            for parTxid in tx.parents:
                if parTxid not in visitedTxnId:
                    return False

        return True

    def print(self):
        print("transactions: {}".format(self.txns))
        print("fee: {}".format(self.fee))
        print("weight: {}\n".format(self.weight))


    def createTxt(self):
        with open('block.txt', 'w') as file_handle:
            for tx in self.txns:
                file_handle.write('{}\n'.format(tx.txid))
