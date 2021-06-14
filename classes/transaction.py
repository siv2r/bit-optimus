class Transaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = [] if (not parents) else parents.split(';')
        self.visited = False

    def isVisited(self):
        return self.visited

    def print(self):
        print("id: {}".format(self.txid))
        print("fee: {}".format(self.fee))
        print("weight: {}".format(self.weight))
        print("parents: {}".format(self.parents))
        print("visited: {}\n".format(self.visited))
    
    def cntParent(self):
        return len(self.parents)