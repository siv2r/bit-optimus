# Bitcoin-miner
Mining transactions in an optimal way

# Note
1. The 'mempool.csv' has a column name 'parents ' instead of 'parents'.
2. Should we make it list or dict?
3. `weight`, `fee` are of type `int`.

# Approach
- Iteration 1:
  - sort the mempool data by the metric `fee/weight` in descenting order
  - start add transactions to the block till its `weight` is less than `4000000`
  - **Improvement:** Find a single equivalent block for a block + parents  
- Iteration 2: coming soon

# Limitation
- Iteration 1:
  - Not the most optimal since some transaction requires parents to be added. Blindly adding this parent since, its child has good metric is not optimal
- Iteration 2: coming soon

# Result
- Iteration 1:
  - Block fee: 6345335
  - Block weight: 4000000

# Reference
1. https://realpython.com/python-csv/
2. [split() in python](https://stackoverflow.com/questions/16645083/when-splitting-an-empty-string-in-python-why-does-split-return-an-empty-list/16645307)