from classes.transaction import Transaction
from classes.mempool import Mempool


def isValidBlock(mempool):
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


def sortByParentCnt(tx1, tx2):
    parentCnt1 = tx1.cntParent()
    parentCnt2 = tx2.cntParent()

    return parentCnt2 - parentCnt1
