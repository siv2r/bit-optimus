from classes.transaction import Transaction
from classes.mempool import Mempool


class Block():
    def __init__(self, maxWeight=float('inf'), txns=list(), weight=0, fee=0, vis=set()):
        """Constructor for block class

        Args:
            maxWeight (int, optional): Maxmium weight which this block can haven. Defaults to float('inf').
            txns (list, optional): transactions in this block. Defaults to [].
            weight (int, optional): sum of weight of every transactions present. Defaults to 0.
            fee (int, optional): summ of fee of every transaction present. Defaults to 0.
            vis (set, optional): used for marking nodes in DFS. Defaults to set().
        """
        self.txns = txns
        self.weight = weight
        self.fee = fee
        self.visitedEqTxnIds = vis
        self.maxWeight = maxWeight

    def addEqTxn(self, eqTxn, mempool):
        """Adds an equivalent transaction to this block.

        Args:
            eqTxn (Transaction): Combining transaction with its ancestors into a single transaction
            mempool (Mempool): Paresed inputs
        """        
        # mark the eqTxn as visited
        self.visitedEqTxnIds.add(eqTxn.txid)
        eqTxnIds = eqTxn.txid.split('\n')
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
        """Loops through all the equivalent transaction adds them sequentialy along with its parent. NOTE: the equivalen transaction list must be sorted before using this function

        Args:
            mempool (Mempool): Paresed input
        """        
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
        """Creates the block.txt
        """        
        with open('block.txt', 'w') as file_handle:
            for tx in self.txns:
                file_handle.write('{}\n'.format(tx.txid))
