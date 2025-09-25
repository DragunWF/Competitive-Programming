# https://www.codewars.com/kata/54bd06539f075cece0000feb/python

def tick_toward(start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    output = [start]
    current_vector = start
    while current_vector != target:
        x = current_vector[0]
        y = current_vector[1]
        if x != target[0]:
            x += 1 if x < target[0] else -1
        if y != target[1]:
            y += 1 if y < target[1] else -1
        new_vector = (x, y)
        output.append(new_vector)
        current_vector = new_vector
    return output


def test() -> None:
    print(tick_toward(tuple([5, 5]), tuple([5, 7])))  # [(5,5), (5,6), (5,7)]


if __name__ == "__main__":
    test()
