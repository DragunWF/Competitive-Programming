# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AUCTION

def solve() -> None:
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        max_value = max(a, b, c)
        if max_value == a:
            print("Alice")
        elif max_value == b:
            print("Bob")
        else:
            print("Charlie")


if __name__ == "__main__":
    solve()
