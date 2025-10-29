# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRB01


def solve() -> None:
    for _ in range(int(input())):
        n = int(input())
        print("yes" if is_prime(n) else "no")


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    solve()
