from classes.transaction import Transaction
from classes.mempool import Mempool
from classes.block import Block
from functools import cmp_to_key
from functions import *

def main():
    # base variables
    maxWeight = 4000000
    mempool = Mempool('mempool.csv')

    # fill data into mempool from the csv
    mempool.parse_csv()
    mempool.caclAllAncestorCnt()
    mempool.txns.sort(key=cmp_to_key(sortByAncestorCnt))

    mempool.createEqTxnPool()
    # sort the eqTxns by Feerate
    mempool.eqTxns.sort(key=cmp_to_key(sortByFeerate))

    optBlock = Block(maxWeight)
    optBlock.selectOptEqTxns(mempool);
    optBlock.createTxt()

    print("The weight of the block is: {}".format(optBlock.weight))
    print("The fee of the block is: {}".format(optBlock.fee))

    if(isValidBlock(mempool)):
        print('The optimized block is valid')



if __name__ == "__main__":
    main()
