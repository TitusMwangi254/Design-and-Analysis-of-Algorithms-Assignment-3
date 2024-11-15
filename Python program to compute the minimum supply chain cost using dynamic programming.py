def supply_chain_optimization(cost_matrix):
    """
    Compute the minimum supply chain cost using dynamic programming.

    :param cost_matrix: 2D list where cost_matrix[i][j] is the cost of supplying warehouse i by supplier j.
    :return: Minimum cost and the supplier allocation.
    """
    num_warehouses = len(cost_matrix)
    num_suppliers = len(cost_matrix[0])

    # DP table to store the minimum cost up to warehouse i using supplier j
    dp = [[float('inf')] * num_suppliers for _ in range(num_warehouses)]
    # Path table to reconstruct supplier allocation
    path = [[-1] * num_suppliers for _ in range(num_warehouses)]

    # Initialize base case
    for j in range(num_suppliers):
        dp[0][j] = cost_matrix[0][j]

    # Fill the DP table
    for i in range(1, num_warehouses):
        for j in range(num_suppliers):
            for k in range(num_suppliers):
                cost = dp[i-1][k] + cost_matrix[i][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    path[i][j] = k

    # Find the minimum cost in the last row
    min_cost = min(dp[-1])
    last_supplier = dp[-1].index(min_cost)

    # Reconstruct the supplier allocation
    allocation = [last_supplier]
    for i in range(num_warehouses - 1, 0, -1):
        last_supplier = path[i][last_supplier]
        allocation.append(last_supplier)

    allocation.reverse()

    return min_cost, allocation


# Example usage
cost_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

min_cost, allocation = supply_chain_optimization(cost_matrix)
print("Minimum Supply Chain Cost:", min_cost)
print("Supplier Allocation:", allocation)
