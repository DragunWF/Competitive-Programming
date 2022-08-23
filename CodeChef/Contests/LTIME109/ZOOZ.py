t = int(input())
for i in range(t):
    n = int(input())
    print(f"1{'0' * (n - 2)}1" if n != 3 else "010")
