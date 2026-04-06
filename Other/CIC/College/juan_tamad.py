def solve() -> None:
    k = int(input("Enter the maximum number of trees to pick: "))
    n = int(input("Enter the number of available trees: "))
    trees = []
    for i in range(n):
        trees.append(int(input()))
    trees.sort(reverse=True)

    total = 0
    for i in range(min(k, n)):
        total += trees[i]
    print(f"Maximum number of fruits: {total}")


if __name__ == "__main__":
    solve()
