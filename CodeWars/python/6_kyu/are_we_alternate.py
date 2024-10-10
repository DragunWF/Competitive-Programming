# https://www.codewars.com/kata/59325dc15dbb44b2440000af/train/python

def is_alt(s: str) -> bool:
    VOWELS = "aeiouAEIOU"
    alternate_cog = s[0] in VOWELS  # Serves as an alternating cog
    for i in range(len(s)):
        if (not alternate_cog and s[i] in VOWELS) or (alternate_cog and not s[i] in VOWELS):
            return False
        alternate_cog = not alternate_cog
    return True


def test():
    # Not part of the solution, just testing
    print(is_alt("amazon"))  # True
    print(is_alt("apple"))  # False


if __name__ == "__main__":
    test()
