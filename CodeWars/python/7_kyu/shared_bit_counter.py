# https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python

def shared_bits(a: int, b: int) -> bool:
    binary_a = bin(a)[2:][::-1]
    binary_b = bin(b)[2:][::-1]
    shared_bit_count = 0
    for i in range(min(len(binary_a), len(binary_b))):
        if binary_a[i] == "1" and binary_b[i] == "1":
            shared_bit_count += 1
            if shared_bit_count >= 2:
                return True
    return False
