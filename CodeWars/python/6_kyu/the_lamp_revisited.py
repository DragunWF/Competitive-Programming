# https://www.codewars.com/kata/570e6e32de4dc8a8340016dd/train/python

class Lamp:
    def __init__(self, color: str):
        self.color = color
        self.on = False

    def state(self) -> str:
        return f"The lamp is {'on' if self.on else 'off'}."

    def toggle_switch(self) -> None:
        self.on = not self.on


def test() -> None:
    lamp = Lamp("Blue")
    print(lamp.color)
    print(lamp.on)
    print(lamp.state())
    lamp.toggle_switch()
    print(lamp.state())


if __name__ == "__main__":
    test()
