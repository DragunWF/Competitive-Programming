t = int(input())
for i in range(t):
    w, x, y, z = map(int, input().split(" "))
    weights = (x + y, x + z, y + z, x + y + z, x, y, z)
    exact_measurement = False
    for value in weights:
        if value == w:
            exact_measurement = True
            break
    print("YES" if exact_measurement else "NO")
