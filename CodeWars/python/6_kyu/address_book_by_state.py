# https://www.codewars.com/kata/59d0ee709f0cbcf65400003b/train/python

def by_state(s: str) -> str:
    states = {'AZ': 'Arizona',
              'CA': 'California',
              'ID': 'Idaho',
              'IN': 'Indiana',
              'MA': 'Massachusetts',
              'OK': 'Oklahoma',
              'PA': 'Pennsylvania',
              'VA': 'Virginia'}
    friends_per_state: dict[str, list[str]] = {}

    friends = s.split("\n")
    for friend in friends:
        if not friend:
            continue

        details = " ".join([item.strip() for item in friend[:-2].split(",")])
        state = friend.strip()[-2:]
        friend_line_item = f"{details} {states[state]}"
        if not state in friends_per_state:
            friends_per_state[state] = [friend_line_item]
        else:
            friends_per_state[state].append(friend_line_item)

    lines = []
    for state in states:
        if state in friends_per_state:
            lines.append(states[state] if not len(lines) else f" {states[state]}")
            for friend in sorted(friends_per_state[state]):
                lines.append(f"..... {friend}")

    return "\r\n".join(lines)


class TestCase:
    def __init__(self, s: str, expected: str):
        self.s = s
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        TestCase("""John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA""",
                 "Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th Street Boston Massachusetts\r\n Virginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia"),
        TestCase("""John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
Terry Kalkas, 402 Lans Road, Beaver Falls PA
Eric Adams, 20 Post Road, Sudbury MA
Hubert Sims, 328A Brook Road, Roanoke MA
Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
Sal Carpenter, 73 6th Street, Boston MA""",
                 "California\r\n..... Amy Wilde 334 Bayshore Pkwy Mountain View California\r\n Massachusetts\r\n..... Eric Adams 20 Post Road Sudbury Massachusetts\r\n..... Hubert Sims 328A Brook Road Roanoke Massachusetts\r\n..... John Daggett 341 King Road Plymouth Massachusetts\r\n..... Sal Carpenter 73 6th Street Boston Massachusetts\r\n Oklahoma\r\n..... Orville Thomas 11345 Oak Bridge Road Tulsa Oklahoma\r\n Pennsylvania\r\n..... Terry Kalkas 402 Lans Road Beaver Falls Pennsylvania\r\n Virginia\r\n..... Alice Ford 22 East Broadway Richmond Virginia")
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = by_state(item.s)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.s}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
