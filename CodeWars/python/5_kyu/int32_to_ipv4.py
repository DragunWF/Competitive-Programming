# https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python

def int32_to_ip(int32: int) -> str:
    first_octet = int32 % 256
    second_octet = int32 % (256 ** 2) // 256
    third_octet = int32 % (256 ** 3) // (256 ** 2)
    fourth_octet = int32 % (256 ** 4) // (256 ** 3)
    return f"{fourth_octet}.{third_octet}.{second_octet}.{first_octet}"


def test() -> None:
    # Calculation Testing
    n = 2149583361
    print(n % 256)  # 1
    print(n % (256 ** 2) // 256)  # 10
    print(n % (256 ** 3) // (256 ** 2))  # 32
    print(n % (256 ** 4) // (256 ** 3))  # 128

    # Test Cases
    print(int32_to_ip(2149583361))  # "128.32.10.1"
    print(int32_to_ip(32))  # "0.0.0.32"
    print(int32_to_ip(0))  # "0.0.0.0"


if __name__ == "__main__":
    test()
