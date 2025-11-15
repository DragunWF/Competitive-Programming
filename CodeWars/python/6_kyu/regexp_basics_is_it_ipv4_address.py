# https://www.codewars.com/kata/567fe8b50c201947bc000056/train/python

def ipv4_address(address: str) -> str:
    octets = address.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or (len(octet) >= 2 and octet.startswith("0")):
            return False
        value = int(octet)
        if not (0 <= value <= 255):
            return False
    return True


def test() -> None:
    print(ipv4_address("10.20.30.40"))  # True


if __name__ == "__main__":
    test()
