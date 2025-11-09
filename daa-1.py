# Fibonacci using recursion and iteration with step count

# -------- Recursive Fibonacci --------
steps_recursive = 0  # Global variable to count steps for recursion


def fibonacci_recursive(n):
    global steps_recursive
    steps_recursive += 1  # Count each function call as one step

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# -------- Iterative Fibonacci --------
def fibonacci_iterative(n):
    steps_iterative = 0  # Local variable to count steps
    a, b = 0, 1

    if n == 0:
        steps_iterative += 1
        return 0, steps_iterative
    elif n == 1:
        steps_iterative += 1
        return 1, steps_iterative

    for i in range(2, n + 1):
        steps_iterative += 1  # Count each loop iteration as one step
        a, b = b, a + b

    return b, steps_iterative


# -------- Main Program --------
n = int(input("Enter the term (n): "))

# Recursive method
steps_recursive = 0
result_recursive = fibonacci_recursive(n)
print("\n--- Recursive Method ---")
print(f"Fibonacci({n}) = {result_recursive}")
print(f"Total steps (recursive calls): {steps_recursive}")

# Iterative method
result_iterative, steps_iterative = fibonacci_iterative(n)
print("\n--- Iterative Method ---")
print(f"Fibonacci({n}) = {result_iterative}")
print(f"Total steps (loop iterations): {steps_iterative}")
