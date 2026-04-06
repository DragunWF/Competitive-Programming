def solve() -> None:
    n = int(input("Enter N: "))

    s = input("Enter secret word: ")
    g = input("Enter guessed word: ")
    feedback = []
    for i in range(n):
        if s[i] == g[i]:
            feedback.append("G")
        else:
            feedback.append("Y" if s[i] in g else "B")

    print(f"Feedback: {''.join(feedback)}")


if __name__ == "__main__":
    solve()
