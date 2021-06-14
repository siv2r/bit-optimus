# Bitcoin-miner
Mining transactions in an optimal way

# Theory behind the challenge (Miner Fee)
- amount sent = amount recieved + transaction fee
- Bitcoins design makes it easier for the sender to specify the `transaction fee` than the reciever. This makes sense since, the `transaction fee` is taken from the sender's wallet.
- When a miner creates a `block proposal`, the miner is entitled to specify where all the fees paid by the transactions in that block proposal should be sent. If the proposal results in a valid block that becomes a part of the best block chain, the fee income will be sent to the specified recipient. If a valid block does not collect all available fees, the amount not collected are permanently destroyed
- To select the set of optimal transaction, miner has to solve two problems
  - **Problem1**: Transaction Fee and Size - Knapsack Problem - NP Hard
  - **Problem2**: Transaction conflicts - Maximum Independent Set Problem - NP Hard

# Problem Statement
Create a block from the pending transactions (`mempool.csv`) that has maximum possible `Miner Fee`

- ## Constraints
  - Block weight should not exceed `4,000,000`
  - Parent transaction should be included before child transaction

# Approach
- ## Intermediate Approach:
  - sort the mempool data by `feerate` in descenting order
  - start add transactions to the block till its `weight` is less than `4000000`
  - **Improvement:** Find a single equivalent block for a block + parents  
- ## Final Approach:
  - Sort the mempool data by number of parents in descending order
  - If a transaction has any parent then calculate an equivalent block by combining child block with its parent (Now this equivalent block can be compared with any block present in the mempool)
  - Sort the mempool by `feerate` in descending order
  - **Improvement** Time complexity of `findIndex()` method in `Mempool class` can be improved

# Limitation
- ## Intermediate Approach:
  - Not the most optimal since some transaction requires parents to be added. Blindly adding this parent since, its child has good metric is not optimal
- ## Final Approach: 
  - 

# Result
- ## Intermediate Approach:
  - Block fee: 6345335
  - Block weight: 4000000
- ## Final Approach:
  - Block fee: 9065240
  - Block weight: 3992164


# Note
1. The `mempool.csv` has a column name `parents_`* instead of `parents`.
2. `weight`, `fee` are of type `int`.
`*` `_` above denotes space

# Reference
- [Bitcoin Mining is NP Hard](https://freedom-to-tinker.com/2014/10/27/bitcoin-mining-is-np-hard/)
- [Miner's Fee article](https://en.bitcoin.it/wiki/Miner_fees#Technical_info)
- [Parsing CSV in Python](https://realpython.com/python-csv/)
- [split() in python](https://stackoverflow.com/questions/16645083/when-splitting-an-empty-string-in-python-why-does-split-return-an-empty-list/16645307)
- [pass by reference in python](https://realpython.com/python-pass-by-reference/)