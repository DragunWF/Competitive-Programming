def solve(n):
    pairs = 1 if n % 2 == 0 else 0
    prev = (-1, -1)
    for i in range(1, n):
        a = n - i
        if i == a or a == prev[0] and i == prev[1]:
            break
        prev = (i, a)
        pairs += 2
    return pairs


n = int(input())
print(solve(n))
