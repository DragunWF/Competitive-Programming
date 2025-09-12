# https://www.codewars.com/kata/52840d2b27e9c932ff0016ae/train/python

def locate(seq: list, value) -> bool:
    def search(items: list) -> bool:
        for item in items:
            if item == value or type(item) is list and search(item):
                return True
        return False
    return search(seq)


def test() -> None:
    print(locate(['two', 'six', ['five', 'seven'], 'three,nine'], "seven"))


if __name__ == "__main__":
    test()
