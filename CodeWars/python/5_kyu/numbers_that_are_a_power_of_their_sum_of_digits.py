# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python


def pow_sum_dig_term(n: int) -> int:
    # I precomputed the numbers up to a specific term, turned them into a list and then did this for O(1) time complexity
    return [81, 512, 2401, 4913, 5832, 17576, 19683, 234256, 390625, 614656, 1679616, 17210368, 34012224, 52521875, 60466176, 205962976, 612220032, 8303765625, 10460353203, 24794911296, 27512614111, 52523350144, 68719476736, 271818611107, 1174711139837, 2207984167552, 6722988818432, 20047612231936, 72301961339136, 248155780267521, 3904305912313344, 45848500718449031, 81920000000000000, 150094635296999121, 13744803133596058624, 19687440434072265625, 53861511409489970176, 73742412689492826049, 179084769654285362176, 480682838924478847449, 671088640000000000000, 8007313507497959524352, 21048519522998348950643, 23316389970546096340992, 2518170116818978404827136, 14076019706120526112710656, 146853371345156431381127623, 166507350731038802170609664, 213292826014568334917410816, 240984500018808097135911707, 2017516459574609153391845376, 2670419511272061205254504361, 4491199828872408503792328704, 4946966739525117513427734375, 13695791164569918553628942336, 101472439712019470540189876224, 283956682347124706942551243009, 667840509835890864312744140625][n - 1]


def is_special_number(n: int) -> bool:
    # Old function to check if a number is special (Brute force)
    str_num = str(n)
    digit_sum = sum(int(digit) for digit in str_num)
    for exponent in range(2, len(str_num) + 1):
        if digit_sum ** exponent == n:
            return True
    return False


def generate_special_numbers_smart(max_terms: int) -> list[int]:
    # New function to check if a number is special (Optimized)
    special_numbers = set()

    # Need to check much wider ranges to catch all special numbers
    for digit_sum in range(1, 200):  # Increased range
        if digit_sum == 1:
            continue  # Skip 1 as it can't produce valid results

        power = digit_sum * digit_sum  # Start from exponent 2
        exponent = 2

        # Continue until numbers get too large (but be more generous)
        while power < 10**30:  # Much larger limit
            # Check if sum of digits of power equals digit_sum
            actual_digit_sum = sum(int(d) for d in str(power))
            if actual_digit_sum == digit_sum:
                special_numbers.add(power)
                print(
                    f"Found: {power} (digit_sum={digit_sum}, exponent={exponent})")

            power *= digit_sum
            exponent += 1

            # Safety break for very large digit sums
            if exponent > 50:
                break

    # Sort and return the first max_terms
    sorted_numbers = sorted(list(special_numbers))
    print(f"Found {len(sorted_numbers)} special numbers total")
    print(f"Terms: {sorted_numbers}")

    return sorted_numbers[:max_terms]


def generate_pow_sum_dig_terms(n: int) -> int:
    terms = generate_special_numbers_smart(n)
    return terms[n - 1]


def test() -> None:
    # Expected: True
    print(is_special_number(81))

    # Expected: True
    print(is_special_number(4913))

    # Expected: True
    print(is_special_number(5832))

    # Expected: True
    print(is_special_number(3904305912313344))

    # Expected: 81
    # print(pow_sum_dig_term(1))

    # Expected: 512
    # print(pow_sum_dig_term(2))

    # Expected: 2401
    # print(pow_sum_dig_term(3))

    # Expected: 480682838924478847449
    print(generate_pow_sum_dig_terms(40))


if __name__ == "__main__":
    test()
