# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MVR

def solve() -> None:
    a, b, x, y = map(int, input().split())
    messi_points = a * 2 + b
    ronaldo_points = x * 2 + y
    if messi_points == ronaldo_points:
        print("Equal")
        return
    print("Messi" if messi_points > ronaldo_points else "Ronaldo")


if __name__ == "__main__":
    solve()
