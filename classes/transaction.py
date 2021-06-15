class Transaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = [] if (not parents) else parents.split(';')
        self.ancestorCnt = -1

    def print(self):
        print("id: {}".format(self.txid))
        print("fee: {}".format(self.fee))
        print("weight: {}".format(self.weight))
        print("parents: {}\n".format(self.parents))
    
    def cntParent(self):
        return len(self.parents)