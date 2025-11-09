def safe(b, r, c, n):
    for i in range(c):
        if (
            b[r][i]
            or (r - i - 1 >= 0 and b[r - i - 1][c - i - 1])
            or (r + i + 1 < n and b[r + i + 1][c - i - 1])
        ):
            return False
    return True


def solve(b, c, n):
    if c == n:
        for r in b:
            print(r)
        return True
    for r in range(n):
        if safe(b, r, c, n):
            b[r][c] = 1
            if solve(b, c + 1, n):
                return True
            b[r][c] = 0
    return False


n = int(input("Enter N: "))
b = [[0] * n for _ in range(n)]
if not solve(b, 0, n):
    print("No solution for", n)
