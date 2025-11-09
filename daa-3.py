def fractional_knapsack():
    n = int(input("Enter number of items: "))

    weight = []
    value = []

    for i in range(n):
        w = float(input(f"Enter weight of item {i+1}: "))
        v = float(input(f"Enter value of item {i+1}: "))
        weight.append(w)
        value.append(v)

    capacity = float(input("Enter knapsack capacity: "))

    # Calculate value/weight ratio and sort
    ratio = [(value[i] / weight[i], weight[i], value[i]) for i in range(n)]
    ratio.sort(reverse=True)

    total_value = 0

    for r, w, v in ratio:
        if capacity == 0:
            break
        if w <= capacity:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            capacity = 0

    print("\nMaximum value in knapsack =", total_value)


# ---- Main ----
fractional_knapsack()
