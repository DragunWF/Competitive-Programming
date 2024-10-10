def solve(x, y, a):
    if a < y and a >= x:
        return "YES"
    return "NO"

def main():
    t = int(input())
    for i in range(t):
        x, y, a = map(int, input().split(" "))
        print(solve(x, y, a))

main()
