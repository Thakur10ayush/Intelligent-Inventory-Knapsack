def fractional_knapsack(items, capacity):
    """
    Solves the Fractional Knapsack problem using a Greedy approach.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    sorted_items = sorted(items, key=lambda x: x['profit'] / x['weight'], reverse=True)
    
    total_profit = 0.0
    remaining_capacity = capacity
    selected_items = []

    for item in sorted_items:
        if remaining_capacity == 0:
            break
            
        if item['weight'] <= remaining_capacity:
            selected_items.append({
                'name': item['name'],
                'weight_taken': item['weight'],
                'profit_earned': item['profit'],
                'fraction': 1.0
            })
            total_profit += item['profit']
            remaining_capacity -= item['weight']
        else:
            fraction = remaining_capacity / item['weight']
            profit_earned = item['profit'] * fraction
            selected_items.append({
                'name': item['name'],
                'weight_taken': remaining_capacity,
                'profit_earned': round(profit_earned, 2),
                'fraction': round(fraction, 2)
            })
            total_profit += profit_earned
            remaining_capacity = 0

    return round(total_profit, 2), selected_items