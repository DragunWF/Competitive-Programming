# www.codechef.com/practice/course/logical-problems/DIFF800/problems/DICEGAME2

def solve() -> None:
    for _ in range(int(input())):
        values = list(map(int, input().split()))
        alice_rolls = values[0:3]
        bob_rolls = values[3:]
        alice_rolls.sort()
        bob_rolls.sort()

        alice_sum = alice_rolls[-1] + alice_rolls[-2]
        bob_sum = bob_rolls[-1] + bob_rolls[-2]
        if alice_sum == bob_sum:
            print("Tie")
            continue
        print("Alice" if alice_sum > bob_sum else "Bob")


if __name__ == "__main__":
    solve()
