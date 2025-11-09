def knapsack():
    n = int(input("Enter number of items: "))
    weight = []
    value = []

    for i in range(n):
        w = int(input(f"Enter weight of item {i+1}: "))
        v = int(input(f"Enter value of item {i+1}: "))
        weight.append(w)
        value.append(v)

    capacity = int(input("Enter capacity of knapsack: "))

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:  # if current item can fit
                include = value[i - 1] + dp[i - 1][w - weight[i - 1]]  # include item
                exclude = dp[i - 1][w]  # exclude item
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]  # can't include item

    print("\nMaximum profit =", dp[n][capacity])


# --- Main ---
knapsack()
