# https://www.codewars.com/kata/simple-encryption-number-2-index-difference

from string import ascii_lowercase, ascii_uppercase, digits


def encrypt(text: str) -> str:
    if not text:
        return text

    region = f"{ascii_uppercase}{ascii_lowercase}{digits}.,:;-?! '()$%&\""
    region_map = to_region_map(region)
    encrypted_text = ""

    # Step 1
    for i, char in enumerate(text):
        if not char in region:
            raise Exception("Character is not in the region!")
        if (i + 1) % 2 == 0:
            encrypted_text += char.upper() if char.islower() else char.lower()
        else:
            encrypted_text += char

    # Step 2
    N = len(encrypted_text)
    step_1_text = encrypted_text
    encrypted_text = [*encrypted_text]
    for i in range(1, N):
        new_index = (region_map[step_1_text[i - 1]] -
                     region_map[step_1_text[i]]) % 77
        encrypted_text[i] = region[new_index]

    # Step 3
    encrypted_text[0] = region[76 - region_map[encrypted_text[0]]]

    return "".join(encrypted_text)


def decrypt(encrypted_text: str) -> str:
    if not encrypted_text:
        return encrypted_text

    region = f"{ascii_uppercase}{ascii_lowercase}{digits}.,:;-?! '()$%&\""
    region_map = to_region_map(region)

    if any(not char in region for char in encrypted_text):
        raise Exception("Character is not in the region!")

    # Reverse Step 3 Encryption
    decrypted_text = [*encrypted_text]
    decrypted_text[0] = region[76 - region_map[decrypted_text[0]]]

    # Reverse Step 2 Encryption
    N = len(decrypted_text)
    for i in range(1, N):
        previous_char = decrypted_text[i - 1]
        char = decrypted_text[i]
        new_index = (region_map[previous_char] - region_map[char]) % 77
        decrypted_text[i] = region[new_index]

    # Reverse Step 1 Encryption
    for i in range(1, N):
        if (i + 1) % 2 == 0:
            char = decrypted_text[i]
            decrypted_text[i] = char.upper(
            ) if char.islower() else char.lower()

    return "".join(decrypted_text)


def to_region_map(region: str) -> str:
    region_map = {}
    for i, char in enumerate(region):
        region_map[char] = i
    return region_map


def test() -> None:
    print(encrypt("Business"))  # &61kujla
    print(encrypt("This is a test!"))  # 5MyQa9p0riYplZc

    print(decrypt("&61kujla"))  # Business
    print(decrypt("5MyQa9p0riYplZc"))  # This is a test!

    print(decrypt("$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"))


if __name__ == "__main__":
    test()
