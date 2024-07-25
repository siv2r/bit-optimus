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

    # calculate no of ancestors for every node and sort them by this factor
    mempool.caclAllAncestorCnt()
    mempool.txns.sort(key=cmp_to_key(sortByAncestorCnt))

    # create equivalent transactions (ie, combine ancestors with child) and sort transactions by feerate
    mempool.createEqTxnPool()
    mempool.eqTxns.sort(key=cmp_to_key(sortByFeerate))

    # select optimal blocks from the equivalent transaction greedily
    optBlock = Block(maxWeight)
    optBlock.selectOptEqTxns(mempool);
    optBlock.createTxt()

    # print the block values
    print("Block Weight: {}".format(optBlock.weight))
    print("Block Fee: {}".format(optBlock.fee))

    # check validity of block
    if(isValidBlock(mempool)):
        print('The optimized block is valid')



if __name__ == "__main__":
    main()
