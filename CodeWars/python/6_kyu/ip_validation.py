# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_IP(ip: str) -> bool:
    if "\n" in ip:
        return False
    nums = ip.split(".")
    if len(nums) != 4:
        return False
    for value in nums:
        if (not len(value) or
            len(value) > 1 and value[0] == "0" or
            value[0] == " " or value[-1] == " "):
            return False
        try:
            num = int(value)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True
