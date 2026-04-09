# https://www.codewars.com/kata/69bf57993a0061ef6d03c095/train/python

def calculate(price_dict: dict, transaction: str) -> int:
    current_digit = []
    added_transactions = []
    for char in transaction:
        if char.isdigit() or char == "-":
            current_digit.append(char)
        else:
            if not current_digit:
                for i, item in enumerate(added_transactions):
                    if item[0] == char:
                        added_transactions.pop(i)
                        break
                continue
            item_count = int("".join(current_digit))
            added_transactions.insert(0, ((char, price_dict[char] * item_count)))
            current_digit.clear()

    total_price = 0
    for item in added_transactions:
        total_price += item[1]
    return total_price


class TestCase:
    def __init__(self, price_dict: dict, transaction: str, expected: int):
        self.price_dict = price_dict
        self.transaction = transaction
        self.expected = expected


def test() -> None:
    test_cases: list[TestCase] = [
        # Original
        TestCase({"A": 1, "B": 3, "C": 2}, "1A2BA3AC4CA", 14),

        # Basic Tests
        TestCase({"X": 0, "Y": 0, "Z": 0}, "5X6Y20Z1X6Y", 0),
        TestCase({"R": 1, "Q": 2, "E": 3, "X": 4}, "4R1Q4X2E1R2X", 37),
        TestCase({"T": 12, "F": 6}, "2F5T1T", 84),
        TestCase({"G": 1, "M": 1, "F": 1, "H": 1, "J": 1}, "5J2F7M1H9G6M1H", 31),
        TestCase({"E": 67}, "1E", 67),

        # Negative Digits
        TestCase({"X": 3, "Y": 3, "Z": 3}, "2X-1Y7X2Z-1Z9Y5X-3Y", 60),
        TestCase({"W": 12}, "9W6W-2W8W5W-4W1W", 276),

        # More than 1 Digit
        TestCase({"X": 1, "Y": 2, "Z": 5}, "10X22Y12Z2X", 116),
        TestCase({"K": 0, "P": 2, "B": 6, "M": 4}, "50K10P42B521M4K125B", 3106),

        # Basic Cancellations
        TestCase({"A": 3, "B": 1, "C": 4}, "3C2B1AC", 5),
        TestCase({"D": 6, "B": 10, "G": 2}, "5D4GG6B2D1GBD", 32),

        # Stacked Cancellation
        TestCase({"A": 4, "B": 3, "C": 2, "D": 1}, "6D1A3B5A2C3AAAA", 19),
        TestCase({"S": 12, "I": 56, "G": 2, "M": 1, "A": 8}, "5G1S7M2I9A6SMISGAS", 0),

        # Nothing to be Cancelled
        TestCase({"T": 1, "V": 5}, "6TVTT2V", 10),
        TestCase({"L": 2, "M": 4, "N": 6, "O": 8}, "12LO3MLL5L1O4N", 54),

        # Only Cancels
        TestCase({"W": 2, "D": 4}, "DWDWDWWD", 0)
    ]
    correct_count = 0
    for i, item in enumerate(test_cases):
        result = calculate(item.price_dict, item.transaction)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: {item.price_dict} | {item.transaction}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    print()
    test()
    print()
