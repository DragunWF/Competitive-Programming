# https://www.codewars.com/kata/56484848ba95170a8000004d/train/python

def gps(s: int, x: list[float]) -> int:
    if len(x) <= 1:
        return 0
    calculated_avg_speed = []
    for i in range(1, len(x)):
        delta_distance = abs(x[i] - x[i - 1])
        calculated_avg_speed.append((3600 * delta_distance) / s)
    return int(max(calculated_avg_speed))


def test() -> None:
    x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
    s = 20
    print(gps(s, x))  # 41


if __name__ == "__main__":
    test()
