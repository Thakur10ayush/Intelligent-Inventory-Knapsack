import time
import random
from src.greedy_knapsack import fractional_knapsack
from src.dp_knapsack import zero_one_knapsack

def run_sample_warehouse():
    print("=== SAMPLE WAREHOUSE INVENTORY SCENARIO ===")
    capacity = 50
    products = [
        {"name": "Laptops (Box)", "weight": 10, "profit": 60},
        {"name": "Monitors (Pallet)", "weight": 20, "profit": 100},
        {"name": "Server Racks", "weight": 30, "profit": 120},
        {"name": "Bulk Cables", "weight": 15, "profit": 45},
    ]

    g_profit, g_items = fractional_knapsack(products, capacity)
    dp_profit, dp_items = zero_one_knapsack(products, capacity)

    print(f"\nWarehouse Max Capacity: {capacity} kg")
    print(f"\n[1] Greedy (Fractional) Total Profit: ${g_profit}")
    for item in g_items:
        print(f"   - {item['name']}: {item['weight_taken']} kg (Fraction: {item['fraction']}) -> +${item['profit_earned']}")

    print(f"\n[2] Dynamic Programming (0/1) Total Profit: ${dp_profit}")
    for item in dp_items:
        print(f"   - {item['name']}: {item['weight_taken']} kg -> +${item['profit_earned']}")

def run_performance_benchmark():
    print("\n=== PERFORMANCE BENCHMARK (EXECUTION TIME & PROFIT) ===")
    print(f"{'Items (n)':<12} | {'Capacity (W)':<14} | {'Greedy Time (ms)':<18} | {'DP Time (ms)':<15} | {'Greedy Profit':<15} | {'0/1 DP Profit':<15}")
    print("-" * 98)

    test_cases = [(10, 50), (100, 500), (500, 2000), (1000, 5000)]
    random.seed(42)

    for n, cap in test_cases:
        items = [
            {"name": f"Item_{i}", "weight": random.randint(1, 50), "profit": random.randint(10, 500)}
            for i in range(n)
        ]

        start = time.perf_counter()
        g_profit, _ = fractional_knapsack(items, cap)
        g_time = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        dp_profit, _ = zero_one_knapsack(items, cap)
        dp_time = (time.perf_counter() - start) * 1000

        print(f"{n:<12} | {cap:<14} | {g_time:<18.4f} | {dp_time:<15.4f} | {g_profit:<15.2f} | {dp_profit:<15.2f}")

if __name__ == "__main__":
    run_sample_warehouse()
    run_performance_benchmark()