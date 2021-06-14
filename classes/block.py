from classes.transaction import Transaction
from classes.mempool import Mempool

class Block():
    def __init__(self, maxWeight = float('inf')):
        self.txns = []
        self.weight = 0
        self.fee = 0
        self.visited = set()
        self.maxWeight = maxWeight
    
    def add(self, tx, mempool):
        if tx.weight+self.weight > self.maxWeight:
            raise Exception('Exceeding max block weight')

        self.txns.append(tx)
        self.weight += tx.weight
        self.fee += tx.fee

        # mark transaction as visited
        individualTxnIds = tx.txid.split('\n')
        for individualTxnId in individualTxnIds:
            self.visited.add(individualTxnId)

    def print(self):
        print("transactions: {}".format(self.txns))
        print("fee: {}".format(self.fee))
        print("weight: {}\n".format(self.weight))


    def createTxt(self):
        with open('block.txt', 'w') as file_handle:
            for tx in self.txns:
                file_handle.write('{}\n'.format(tx.txid))
