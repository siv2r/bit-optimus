class Transaction():
    def __init__(self, txid, fee, weight, parents, ancesCnt=-1):
        """Object that is used to store a transaction

        Args:
            txid (str): hash of a transaction
            fee (int): miners fee (i.e, the fee that a miner gets for including this transaction in their block)
            weight (int): size of this transaction
            parents (list): dependencies for this transaction
            ancesCnt (int, optional): number of ancestors for this transaction. Defaults to -1.
        """        
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = [] if (not parents) else parents.split(';')
        self.ancestorCnt = ancesCnt

    def print(self):
        print("id: {}".format(self.txid))
        print("fee: {}".format(self.fee))
        print("weight: {}".format(self.weight))
        print("parents: {}\n".format(self.parents))
    
    def cntParent(self):
        return len(self.parents)