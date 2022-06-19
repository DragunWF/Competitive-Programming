t = int(input())
for i in range(t):
    p, q = map(int, input().split(" "))
    turns = p + q + 1
    alice_turns = (1, 2, 5, 6, 9, 0)
    if turns > 10:
        alice_turns = (3, 4, 7, 8)
    last_number = int(str(turns)[-1])
    print("Alice" if last_number in alice_turns else "Bob")