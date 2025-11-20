# https://www.codewars.com/kata/541a354c39c5efa5fa001372/train/python

def ip_to_num(ip: str) -> int:
    ipv4_values = ip.split(".")
    binary_octets = []
    for value in ipv4_values:
        binary_octets.append(convert_to_bin(int(value)))
    return int("".join(binary_octets), 2)


def convert_to_bin(num: int, required_digit_count: int = 8) -> str:
    str_num = bin(num)[2:]
    padded_zeros = "0" * (required_digit_count - len(str_num))
    return f"{padded_zeros}{str_num}"


def num_to_ip(num: int) -> str:
    binary_num = convert_to_bin(num, 32)
    octets = []
    current_octet = []
    for i, digit in enumerate(binary_num):
        current_octet.append(digit)
        if (i + 1) % 8 == 0:
            octets.append("".join(current_octet))
            current_octet.clear()
    return ".".join(str(int(octet, 2)) for octet in octets)


def test() -> None:
    print(ip_to_num('192.168.1.1'))  # converts to 3232235777
    print(ip_to_num('10.0.0.0'))    # converts to  167772160
    print(ip_to_num('176.16.0.1'))  # converts to 2953838593

    print(num_to_ip(3232235777))  # converts to '192.168.1.1'
    print(num_to_ip(167772160))  # converts to    '10.0.0.0'
    print(num_to_ip(2953838593))  # converts to  '176.16.0.1'


if __name__ == "__main__":
    test()
