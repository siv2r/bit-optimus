from classes.block import Block
from classes.mempool import Mempool
from classes.transaction import Transaction
from functools import cmp_to_key

def cmp(tx1, tx2):
    metric1 = tx1.fee/tx1.weight
    metric2 = tx2.fee/tx2.weight

    return metric2 - metric1


def calcBlock(mempool, maxWeight):

    # sort the mempool
    mempool.txns.sort(key=cmp_to_key(cmp))

    # mempool.print()

    newBlock = Block(maxWeight)

    for tx in mempool.txns:
        newBlock.add(tx, mempool)
        if newBlock.weight >= maxWeight :
            break

    return newBlock


