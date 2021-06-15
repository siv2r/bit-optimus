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
- ## Intermediate Approach 1:
  - sort the mempool data by `feerate` in descenting order
  - start add transactions to the block till its `weight` is less than `4000000`
  - **Improvement:** Find a single equivalent block for a block + parents  
- ## Intermediate Approach 2:
  - If a transaction has any parent then calculate an equivalent block by combining child block with its parent (Now this equivalent block can be compared with any block present in the mempool)
  - Sort the mempool by `feerate` in descending order
  - **Improvement** Try to make sure that you create a equivalent transaction which has more number of ancestors first. For the Example: `a->b->c`, we must hit `a` before `b or c` while creating equivalent transaction
- ## Final Approach:
  - Sort the mempool by number of ancestors present for a transction in descending order
  - Follow the same steps from `Intermediate Approach 2` above
  - **Improvement** Time complexity of `findTxnIndex()`, `findEqTxnIndex()` methods in `Mempool class` can be improved using `dictionary` (looping through list in current implementation)

# Limitations
- ## Intermediate Approach:
  - Not the most optimal since some transaction requires parents to be added. Blindly adding this parent since, its child has good metric is not optimal
- ## Final Approach: 
  - Hopefully none
  - Time complexity of few functions like `findTxnIndex()`, `findEqTxnIndex()` can be improved

# Result
- ## Intermediate Approach 1: 
  - **Block fee:** 6345335 (Incorrect)
  - **Block weight:** 4000000 (Incorrect)
  - The above result are incorrect, the generated `block.txt` was not valid
- ## Intermediate Approach 2:
  - **Block fee:** 5714810
  - **Block weight:** 3999804
- ## Final Approach:
  - **Block fee:** 5797979
  - **Block weight:** 3999808

# My Learnings
- Revisited NP Hard, 0/1 Knapsack, Dynamic Programming
- Better understanding of DFS
- Learnt the Miner's Fee concept. Hence, got a good overview of bitcoin mining process
- Better understanding of python function and internals 
  - Reading CSV files
  - variable assignment
  - how python passes arguments (It is neither pass by value not pass by reference)
  - Debugging python using vscode

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