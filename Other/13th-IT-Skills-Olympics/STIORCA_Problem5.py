def solve() -> None:
    seconds = int(input("Enter the number of seconds (1000 - 86400): "))
    time = float(seconds / 3600)
    values = str(time).split(".")
    hour = values[0]
    minutes_value = float(f"0.{values[1]}") * 60
    minutes = str((minutes_value).__floor__())
    if len(minutes) < 2:
        minutes = f"0{minutes}"
    if len(hour) < 2:
        hour = f"0{hour}"
    print(f"Military Time: {hour}:{minutes}")

    hour_value = int(hour)
    standard_time_hour = int(f"{hour_value - 12 if hour_value > 12 else hour}")
    standard_time = f"{standard_time_hour}:{minutes}"
    if seconds == 86400 and standard_time == "12:00":
        print(f"Standard Time: {standard_time} MN")
    elif seconds == 43200 and standard_time == "12:00":
        print(f"Standard Time: {standard_time} NN")
    elif hour_value >= 12:
        print(f"Standard Time: {standard_time} PM")
    else:
        print(f"Standard Time: {standard_time} AM")


if __name__ == "__main__":
    solve()