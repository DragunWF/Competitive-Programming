# https://www.codewars.com/kata/526989a41034285187000de4

def ips_between(start: str, end: str) -> int:
    start_ipv4 = list(map(int, start.split(".")))
    end_ipv4 = list(map(int, end.split(".")))
    total_ips_between = 0
    total_ips_between += (end_ipv4[3] - start_ipv4[3])
    total_ips_between += (end_ipv4[2] - start_ipv4[2]) * 256
    total_ips_between += (end_ipv4[1] - start_ipv4[1]) * 256 ** 2
    total_ips_between += (end_ipv4[0] - start_ipv4[0]) * 256 ** 3
    return total_ips_between


def test() -> None:
    print(ips_between("10.0.0.0", "10.0.0.50"))  # 50
    print(ips_between("10.0.0.0", "10.0.1.0"))  # 256
    print(ips_between("20.0.0.10", "20.0.1.0"))  # 256
    print(ips_between("10.11.12.13", "10.11.13.0"))  # 243


if __name__ == "__main__":
    test()
