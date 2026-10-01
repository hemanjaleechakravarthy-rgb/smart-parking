\# Algorithm Complexity Analysis



\## 1. Greedy Algorithm



The greedy parking allocation algorithm searches for suitable available slots and selects the slot with minimum distance from the entrance.



\- Time Complexity: O(n)

\- Space Complexity: O(n)

\- Approach: Greedy



\## 2. Divide and Conquer



The divide-and-conquer algorithm divides the available parking slots into smaller sections and recursively finds the nearest slot in each section.



\- Time Complexity: O(n)

\- Space Complexity: O(log n) recursion stack

\- Approach: Divide and Conquer



\## 3. Dynamic Programming



The dynamic programming algorithm uses a two-dimensional DP table to select the required number of slots while minimizing total distance.



\- Time Complexity: O(n × k)

\- Space Complexity: O(n × k)

\- Approach: Dynamic Programming

\- n = number of available slots

\- k = number of required slots



\## 4. Backtracking



The backtracking algorithm explores different combinations of parking slots and keeps the best valid solution.



\- Time Complexity: O(2^n) in the worst case

\- Space Complexity: O(n)

\- Approach: Backtracking



\## 5. Branch and Bound



The branch-and-bound algorithm explores possible allocations while pruning branches that cannot improve the current best solution.



\- Worst-case Time Complexity: O(2^n)

\- Space Complexity: O(n)

\- Approach: Branch and Bound



\## Performance Evaluation



The algorithms were benchmarked using parking lot sizes of 5, 10, 15, 20, and 25 slots.



The benchmark measures average execution time over multiple repetitions. The results are stored in:



`benchmarks/results.csv`



The performance graph is generated as:



`benchmarks/performance\_graph.png`



The benchmark demonstrates that algorithmic complexity affects execution time as the parking lot size increases.

