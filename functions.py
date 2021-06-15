from classes.transaction import Transaction
from classes.mempool import Mempool


def isValidBlock(mempool):
    """Function to check the validity of generated block.txt

    Args:
        mempool (Mempool): Mempool object that has parsed input

    Raises:
        Exception: If any transaction is repeated (ie, double spending)
        Exception: If parent of a transaction is not included before it

    Returns:
        boolean: True if the block is valid
    """
    visitedTxnId = set()

    with open('block.txt', 'r') as file_handle:
        for line in file_handle:
            txid = line.strip('\n')
            if txid in visitedTxnId:
                raise Exception(
                    'The txid: {} is repeated in the block'.format(txid))
                return False
            # mempool.txns[2660].print()
            txIdx = mempool.findTxnIndex(txid)
            tx = mempool.txns[txIdx]
            for parTxid in tx.parents:
                if parTxid not in visitedTxnId:
                    raise Exception(
                        'The parent:{} of txid: {} is not included'.format(parTxid, txid))
                    return False

            visitedTxnId.add(txid)

        return True


def sortByFeerate(tx1, tx2):
    feerate1 = tx1.fee/tx1.weight
    feerate2 = tx2.fee/tx2.weight

    return feerate2 - feerate1


def sortByAncestorCnt(tx1, tx2):
    ancestorCnt1 = tx1.ancestorCnt
    ancestorCnt2 = tx2.ancestorCnt

    if ancestorCnt1 == -1 or ancestorCnt2 == -1:
        raise Exception('Ancestors not assigned')

    return ancestorCnt2 - ancestorCnt1
