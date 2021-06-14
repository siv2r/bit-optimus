from classes.block import Block
from classes.mempool import Mempool
from classes.transaction import Transaction

def calcBlock(mempool):
    newBlock = Block()

    for tx in mempool.txns:
        newBlock.add(tx)
        if newBlock.weight > 10000:
            break

    return newBlock


