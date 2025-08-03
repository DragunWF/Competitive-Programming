# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python

def ip_to_int32(ip: str) -> str:
    nums = [int(octet) for octet in ip.split(".")]
    return (nums[0] * 256 ** 3) + (nums[1] * 256 ** 2) + (nums[2] * 256) + nums[3]


def test() -> None:
    print(ip_to_int32("128.32.10.1"))  # 2149583361


if __name__ == "__main__":
    test()
