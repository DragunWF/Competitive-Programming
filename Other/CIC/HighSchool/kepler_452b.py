def solve() -> None:
    n = int(input("Enter number of measurements: "))  # Unused in solution but required input by the problem statement
    measurements = list(map(int, input("Enter measurements: ").split()))
    min_time_steps = int(input("Enter the minimum consecutive time steps for transit: "))
    threshold = max(measurements) * 0.4

    is_transit = False
    consecutive_low_brightness = 0
    for measurement in measurements:
        if measurement <= threshold:
            consecutive_low_brightness += 1
        else:
            consecutive_low_brightness = 0
        if consecutive_low_brightness >= min_time_steps:
            is_transit = True
            break
    print("TRANSIT DETECTED" if is_transit else "NO TRANSIT DETECTED")


if __name__ == "__main__":
    solve()
