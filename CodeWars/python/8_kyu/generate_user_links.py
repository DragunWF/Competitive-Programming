# https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python

from urllib.parse import quote


def generate_link(user: str) -> str:
    username = quote(user)
    return f"http://www.codewars.com/users/{username}"


def test() -> None:
    print(generate_link("DragunWF"))
    print(generate_link("The Animator"))


if __name__ == "__main__":
    test()
