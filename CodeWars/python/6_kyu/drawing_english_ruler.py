# https://www.codewars.com/kata/696fe8b06b4e2e6ddb50caa8

class Ruler:
    def __init__(self, t: int, n: int):
        """
        Args:
            t: major tick length (>= 2)
            n: number of inches (>= 1)
        """
        if t < 2:
            raise ValueError("t must be >= 2")
        if n < 1:
            raise ValueError("n must be >= 1")
        self.t = t
        self.n = n

    def draw(self) -> str:
        """Return the ruler as a newline-separated ASCII string."""
        lines = []
        tick = self.generate_tick()
        for i in range(self.n + 1):
            lines.append(f"{'-' * self.t} {i}")
            if i == self.n:
                break
            lines.append(tick)
        return "\n".join(lines)

    def generate_tick(self) -> str:
        lines = []
        for i in range(1, 2 ** (self.t - 1)):
            binary = bin(i)[2:]
            trailing_zeroes = self.count_trailing_zeroes(binary)
            lines.append("-" * (trailing_zeroes + 1))
        return "\n".join(lines)

    def count_trailing_zeroes(self, bin_str: str) -> int:
        count = 0
        for i in range(len(bin_str) - 1, -1, -1):
            if bin_str[i] == "0":
                count += 1
            else:
                break
        return count


def test() -> None:
    print(Ruler(2, 4).draw())
    print()
    print(Ruler(3, 3).draw())
    print()
    print(Ruler(5, 1).draw())


if __name__ == "__main__":
    test()
