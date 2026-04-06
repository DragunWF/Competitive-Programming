def solve() -> None:
    withdraw_amount = int(input("Enter the amount to withdraw: "))
    denomination_count = 0
    current_amount = withdraw_amount
    bills = {"1000": 0, "500": 0, "100": 0, "50": 0, "10": 0, "5": 0, "1": 0}
    while current_amount > 0:
        # Forgive me father for I have sinned...
        if current_amount >= 1000:
            amount = current_amount // 1000
            denomination_count += amount
            current_amount -= amount * 1000
            bills["1000"] += amount
        elif current_amount >= 500:
            amount = current_amount // 500
            denomination_count += amount
            current_amount -= amount * 500
            bills["500"] += amount
        elif current_amount >= 100:
            amount = current_amount // 100
            denomination_count += amount
            current_amount -= amount * 100
            bills["100"] += amount
        elif current_amount >= 50:
            amount = current_amount // 50
            denomination_count += amount
            current_amount -= amount * 50
            bills["50"] += amount
        elif current_amount >= 10:
            amount = current_amount // 10
            denomination_count += amount
            current_amount -= amount * 10
            bills["10"] += amount
        elif current_amount >= 5:
            amount = current_amount // 5
            denomination_count += amount
            current_amount -= amount * 5
            bills["5"] += amount
        else:
            denomination_count += current_amount
            bills["1"] = current_amount
            current_amount = 0
    for bill in bills:
        print(f"{bills[bill]} bill/s of {bill}")


if __name__ == "__main__":
    solve()
