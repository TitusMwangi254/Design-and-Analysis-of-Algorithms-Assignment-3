import numpy as np

def inventory_optimization(demand, holding_cost, fixed_cost, unit_cost, max_inventory):
    """
    Dynamic programming solution for inventory management.

    :param demand: List of demand for each period.
    :param holding_cost: Cost of holding one unit of inventory per period.
    :param fixed_cost: Fixed cost per order.
    :param unit_cost: Cost per unit ordered.
    :param max_inventory: Maximum allowable inventory.
    :return: Minimum total cost and reorder policy.
    """
    T = len(demand)
    dp = np.full((T + 1, max_inventory + 1), float('inf'))
    reorder = [[0] * (max_inventory + 1) for _ in range(T + 1)]

    # Base case: Zero cost at the end of the planning horizon
    dp[T][:] = 0

    # Fill DP table backwards
    for t in range(T - 1, -1, -1):
        for inventory in range(max_inventory + 1):
            for order_qty in range(max_inventory - inventory + 1):
                new_inventory = inventory + order_qty - demand[t]
                if new_inventory >= 0 and new_inventory <= max_inventory:
                    order_cost = fixed_cost * (order_qty > 0) + unit_cost * order_qty
                    holding_cost_total = holding_cost * new_inventory
                    total_cost = order_cost + holding_cost_total + dp[t + 1][new_inventory]
                    if total_cost < dp[t][inventory]:
                        dp[t][inventory] = total_cost
                        reorder[t][inventory] = order_qty

    # Retrieve optimal policy
    inventory = 0
    policy = []
    for t in range(T):
        policy.append(reorder[t][inventory])
        inventory += reorder[t][inventory] - demand[t]

    return dp[0][0], policy

# Example usage
demand = [10, 20, 15, 10]  # Demand for each period
holding_cost = 2           # Holding cost per unit
fixed_cost = 50            # Fixed ordering cost
unit_cost = 10             # Cost per unit ordered
max_inventory = 50         # Maximum allowable inventory

min_cost, policy = inventory_optimization(demand, holding_cost, fixed_cost, unit_cost, max_inventory)
print("Minimum Total Cost:", min_cost)
print("Reorder Policy:", policy)
