from classes.transaction import Transaction
from classes.mempool import Mempool
from classes.block import Block

def main():
    mempool = Mempool('mempool.csv')
    mempool.parse()
    # mempool.print()

    tx = mempool.txns[993]

    block = Block()
    block.add(tx, mempool)
    if block.isValid():
        print("The block is valid!")
        print("Block weight: {}".format(block.weight))
        print("Block fee: {}".format(block.fee))
    else:
        print("The block is not valid!!")

    block.createTxt()


if __name__ == "__main__":
    main()



