from classes.transaction import Transaction
from classes.mempool import Mempool
from classes.block import Block
from functools import cmp_to_key

def isValid(block, mempool):
    visitedTxnId = set()

    for tx in block.txns:
        if tx in visitedTxId:
            raise Exception('Double counted transaction {}'.format())

        # mark transaction as visited    
        visitedTxnId.add(tx.txid)

        for parTxid in mempool.txns.parents:
            if parTxid not in visitedTxnId:
                return False

    return True

def sortByFeerate(tx1, tx2):
    feerate1 = tx1.fee/tx1.weight
    feerate2 = tx2.fee/tx2.weight

    return feerate2 - feerate1


def sortByParentCnt(tx1, tx2):
    parentCnt1 = tx1.cntParent()
    parentCnt2 = tx2.cntParent()

    return parentCnt2 - parentCnt1


def main():
    maxWeight = 4000000
    mempool = Mempool('mempool.csv')
    mempool.parse_csv()
    # mempool.print()

    # sort by parent count in descending order
    mempool.txns.sort(key=cmp_to_key(sortByParentCnt))
    # create equivalent transaction for the transaction containing dependencies
    mempool.addEqTxnsToPool()
    # sort the eq
    mempool.eqTxns.sort(key=cmp_to_key(sortByFeerate))

    optBlock = Block(maxWeight)

    for tx in mempool.eqTxns:
        if (optBlock.weight + tx.weight <= maxWeight):
            optBlock.add(tx, mempool)
        else:
            break

    optBlock.createTxt()

    print("The weight of the block is: {}".format(optBlock.weight))
    print("The fee of the block is: {}".format(optBlock.fee))


if __name__ == "__main__":
    main()
