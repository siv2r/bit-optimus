from classes.transaction import Transaction
from classes.mempool import Mempool

def main():
    mempool = Mempool('mempool.csv')
    mempool.parse()
    mempool.print()


if __name__ == "__main__":
    main()



