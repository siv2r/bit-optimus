from classes.transaction import Transaction
import csv


class Mempool():
    def __init__(self, fileName, txns=list(), eqTxns=list(), vis=set()):
        """Mempool constructor

        Args:
            fileName (str): name of the input file
            txns (list, optional): list of all the transaction from input file. Defaults to list().
            eqTxns (list, optional): list of equivalent transaction that will be calculated. Defaults to list().
            vis (set, optional): Used when performing DFS. Defaults to set().
        """
        self.fileName = fileName
        self.txns = list()
        self.eqTxns = list()
        self.visitedTxids = set()

    def parse_csv(self):
        """Parsed the input file and fills the transactions into a list
        """
        with open(self.fileName, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            idx = 0
            for line in csv_reader:
                newTxn = Transaction(
                    line['tx_id'], line['fee'], line['weight'], line['parents '])
                self.txns.append(newTxn)

    def createOneEqTxn(self, tx):
        """Creates an equivalent transaction for the given transaction by visiting it ancestors (by DFS) and adding their weight and fees into one

        Args:
            tx (Transaction): Transaction whose equivalent that we need

        Returns:
            Transaction: Calculated equivalent transaction
        """
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
        """Creats a new pool of equivalent transaction by looping through all the input transactions
        """
        # mark visited nodes none
        self.visitedTxids = set()

        for tx in self.txns:
            # if node is visited move to next
            if tx.txid in self.visitedTxids:
                continue

            eqTxn = self.createOneEqTxn(tx)
            self.eqTxns.append(eqTxn)

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

    def AncestorCnt(self, tx):
        """Calculate the number ancestors that a given transaction has

        Args:
            tx (Transaction): input

        Returns:
            int: number ancestor transactions present
        """
        # mark as visited
        self.visitedTxids.add(tx.txid)

        if tx.cntParent() == 0:
            return 0
        else:
            ancestors = 0
            for parId in tx.parents:
                if parId in self.visitedTxids:
                    continue
                parIdx = self.findTxnIndex(parId)
                par = self.txns[parIdx]
                ancestors += self.AncestorCnt(par) + 1

            return ancestors

    def caclAllAncestorCnt(self):
        """Calculates ancestors for all available transactions
        """
        for tx in self.txns:
            # mark all nodes add unvisited
            self.visitedTxids = set()
            tx.ancestorCnt = self.AncestorCnt(tx)

    def print(self):
        record = 0
        for tx in self.txns:
            record += 1
            print("Record {}:".format(record))
            # print the transaction
            tx.print()
