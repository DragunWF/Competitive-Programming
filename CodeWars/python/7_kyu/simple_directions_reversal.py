# https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca/train/python

def solve(arr: list[str]) -> list[str]:
    N = len(arr)
    directions = ["Begin"]
    locations = []
    opposite_direction = {
        "Right": "Left",
        "Left": "Right"
    }

    for i in range(N - 1, -1, -1):
        words = arr[i].split(" ")
        if words[0] in opposite_direction:
            direction = opposite_direction[words[0]]
            directions.append(direction)
        location = " ".join(words[2:])
        locations.append(location)

    output = []
    for i in range(N):
        output.append(f"{directions[i]} on {locations[i]}")
    return output


def test() -> None:
    # ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
    print(solve(["Begin on Road A", "Right on Road B",
          "Right on Road C", "Left on Road D"]))


if __name__ == "__main__":
    test()
