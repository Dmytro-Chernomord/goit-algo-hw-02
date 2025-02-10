# Analysis of Change-Making Algorithms

## Greedy Algorithm

**Complexity:** O(n), where n is the number of coin denominations.

**Working Principle:**
- The algorithm first uses the largest available coin denominations.
- Suitable when the set of coins allows forming any amount correctly.

**Advantages:**
- Simple implementation.
- High execution speed.

**Disadvantages:**
- Does not always find the optimal solution (minimum number of coins).

## Dynamic Programming Algorithm

**Complexity:** O(n * m), where n is the number of denominations and m is the target amount.

**Working Principle:**
- Creates a table of minimum values for each amount up to the target.
- Considers all possible combinations, ensuring the optimal result.

**Advantages:**
- Guarantees finding the minimum number of coins for any amount.

**Disadvantages:**
- Higher complexity compared to the greedy algorithm.
- Requires more memory and time for large amounts.

## Conclusion
- The greedy algorithm works faster but does not always find the optimal solution.
- The dynamic programming algorithm guarantees the best solution but is slower.
- In real cash registers, a combination of both methods may be used to balance speed and optimal change-making.

