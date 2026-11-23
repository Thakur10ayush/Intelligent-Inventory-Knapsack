def zero_one_knapsack(items, capacity):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    n = len(items)
    capacity = int(capacity)
    
    dp = [[0.0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        w_i = int(items[i - 1]['weight'])
        p_i = items[i - 1]['profit']
        
        for w in range(capacity + 1):
            if w_i <= w:
                dp[i][w] = max(p_i + dp[i - 1][w - w_i], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = items[i - 1]
            selected_items.append({
                'name': item['name'],
                'weight_taken': item['weight'],
                'profit_earned': item['profit'],
                'fraction': 1.0
            })
            w -= int(item['weight'])

    selected_items.reverse()
    return round(dp[n][capacity], 2), selected_items