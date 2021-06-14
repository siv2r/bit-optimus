from classes.transaction import Transaction
from classes.mempool import Mempool
from classes.block import Block
from functions.calcBlock import *

def main():
    mempool = Mempool('mempool.csv')
    mempool.parse()
    # mempool.print()

    resultBlock = calcBlock(mempool, 4000000)

    resultBlock.createTxt()

    print("The weight of the block is: {}".format(resultBlock.weight))
    print("The fee of the block is: {}".format(resultBlock.fee))


if __name__ == "__main__":
    main()



