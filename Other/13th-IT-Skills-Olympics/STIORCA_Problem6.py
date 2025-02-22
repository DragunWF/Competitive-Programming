def solve() -> None:
    words = input("Enter a sentence (at least 3 words): ").split(" ")
    if len(words) < 3:
        print("Must be a sentence of at least 3 words")
        return
    print(f"[number of words] = {get_hex_value(len(words))}, contain {len(words)} words")
    header = []
    for i, word in enumerate(words):
        index_hex = get_hex_value(i + 1, 4, False)
        word_len_hex = get_hex_value(len(word), 4, False)
        header.append(f"0x{index_hex}{word_len_hex}")
    print(f"[header]: ( {', '.join(hex_value for hex_value in header)} )")
    for i in range(len(words)):
        words[i] = f"'{words[i]}'"
    print(f"[Data] = list(all Words) [{', '.join(words)}]")

def get_hex_value(count: int, limit=8, prefix=True) -> str:
    value_hex = hex(count)[2:]
    digit_count = len(value_hex)
    hex_value = ((limit - digit_count) * "0") + value_hex
    if prefix:
        return "0x" + hex_value
    return hex_value


if __name__ == "__main__":
    solve()