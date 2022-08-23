def solve(x):
    return "YES" if x > 30 else "NO"
    
t = int(input())
for i in range(t):
    x = int(input())
    print(solve(x))