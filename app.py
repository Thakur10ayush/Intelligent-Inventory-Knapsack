import time
import random
import pandas as pd
import streamlit as st
from src.greedy_knapsack import fractional_knapsack
from src.dp_knapsack import zero_one_knapsack

st.set_page_config(page_title="Intelligent Inventory Knapsack Dashboard", layout="wide")

st.title("Intelligent Inventory Management — Knapsack Optimization")
st.markdown("Compare **Greedy (Fractional Knapsack)** vs. **Dynamic Programming (0/1 Knapsack)** for warehouse profit maximization.")

# Sidebar Controls
st.sidebar.header("Warehouse Configuration")
capacity = st.sidebar.slider("Max Warehouse Capacity (kg)", min_value=10, max_value=200, value=50, step=5)

st.sidebar.subheader("Add Custom Product")
new_name = st.sidebar.text_input("Product Name", "Smartphones (Crate)")
new_weight = st.sidebar.number_input("Weight (kg)", min_value=1, max_value=100, value=12)
new_profit = st.sidebar.number_input("Profit ($)", min_value=1, max_value=1000, value=75)

if "products" not in st.session_state:
    st.session_state.products = [
        {"name": "Laptops (Box)", "weight": 10, "profit": 60},
        {"name": "Monitors (Pallet)", "weight": 20, "profit": 100},
        {"name": "Server Racks", "weight": 30, "profit": 120},
        {"name": "Bulk Cables", "weight": 15, "profit": 45},
    ]

if st.sidebar.button("Add Product"):
    st.session_state.products.append({"name": new_name, "weight": int(new_weight), "profit": float(new_profit)})

if st.sidebar.button("Reset Default Inventory"):
    st.session_state.products = [
        {"name": "Laptops (Box)", "weight": 10, "profit": 60},
        {"name": "Monitors (Pallet)", "weight": 20, "profit": 100},
        {"name": "Server Racks", "weight": 30, "profit": 120},
        {"name": "Bulk Cables", "weight": 15, "profit": 45},
    ]

# Display Current Inventory
st.subheader("1. Available Warehouse Products")
inv_df = pd.DataFrame(st.session_state.products)
inv_df["Profit/Weight Ratio"] = (inv_df["profit"] / inv_df["weight"]).round(2)
st.dataframe(inv_df, use_container_width=True)

# Run Algorithms & Measure Time
start_g = time.perf_counter()
g_profit, g_items = fractional_knapsack(st.session_state.products, capacity)
g_time = (time.perf_counter() - start_g) * 1000

start_dp = time.perf_counter()
dp_profit, dp_items = zero_one_knapsack(st.session_state.products, capacity)
dp_time = (time.perf_counter() - start_dp) * 1000

# Side-by-Side Results
st.subheader("2. Optimization Results Comparison")
col1, col2 = st.columns(2)

with col1:
    st.info("### Greedy Approach (Fractional Knapsack)")
    st.metric("Total Profit", f"${g_profit}", f"Execution: {g_time:.4f} ms")
    st.table(pd.DataFrame(g_items))

with col2:
    st.success("### Dynamic Programming (0/1 Knapsack)")
    st.metric("Total Profit", f"${dp_profit}", f"Execution: {dp_time:.4f} ms")
    st.table(pd.DataFrame(dp_items))

# Visual Profit Chart & Scaling Benchmark
st.subheader("3. Profit & Scalability Analysis")
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("**Total Profit Comparison ($)**")
    profit_chart = pd.DataFrame({
        "Algorithm": ["Greedy (Fractional)", "0/1 DP"],
        "Profit ($)": [g_profit, dp_profit]
    }).set_index("Algorithm")
    st.bar_chart(profit_chart)

with chart_col2:
    st.markdown("**Execution Time Scaling (ms) Across Input Sizes**")
    if st.button("Run Live Scaling Benchmark"):
        sizes = [(10, 50), (100, 500), (300, 1500), (600, 3000)]
        bench_rows = []
        random.seed(42)
        for n, cap in sizes:
            sample = [{"name": f"P_{i}", "weight": random.randint(1, 50), "profit": random.randint(10, 500)} for i in range(n)]
            t0 = time.perf_counter()
            fractional_knapsack(sample, cap)
            tg = (time.perf_counter() - t0) * 1000

            t0 = time.perf_counter()
            zero_one_knapsack(sample, cap)
            tdp = (time.perf_counter() - t0) * 1000

            bench_rows.append({"Items (n)": f"n={n}", "Greedy (ms)": tg, "0/1 DP (ms)": tdp})
        bench_df = pd.DataFrame(bench_rows).set_index("Items (n)")
        st.line_chart(bench_df)
        st.dataframe(bench_df, use_container_width=True)