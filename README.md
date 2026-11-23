# Intelligent Inventory Management Using Knapsack Optimization

## Problem Statement
Develop an inventory selection system that helps a warehouse manager select products to maximize total profit without exceeding a given storage capacity[cite: 1]. Each product has a weight and a profit value[cite: 1]. This project implements both **Greedy (Fractional Knapsack)** and **Dynamic Programming (0/1 Knapsack)** approaches and compares their results and performance across varying inventory sizes[cite: 1].

## Complexity Comparison

| Algorithm | Approach | Time Complexity | Space Complexity | Allows Splitting Items? |
| :--- | :--- | :--- | :--- | :--- |
| **Fractional Knapsack** | Greedy | $O(n \log n)$ | $O(n)$ | Yes |
| **0/1 Knapsack** | Dynamic Programming | $O(n \times W)$ | $O(n \times W)$ | No |

## How to Run
```bash
python benchmark.py