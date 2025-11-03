# https://www.codewars.com/kata/5b65c47cbedf7b69ab00066e

def build_trie(*words: str) -> dict:
    trie = {}
    for word in words:
        current = trie
        for i in range(len(word)):
            prefix = word[0:i+1]
            if prefix not in current:
                current[prefix] = None
            if i < len(word) - 1:
                if current[prefix] is None:
                    current[prefix] = {}
                current = current[prefix]
    return trie


def build_trie_element_old(word: str) -> dict:
    # NOTE: Do not touch this
    element = {word: None}
    for i in range(len(word) - 1, 0, -1):
        prefix = word[0:i]
        element = {prefix: element}
    return element


def test() -> None:
    print(build_trie("trie", "that"))
    print(build_trie("A", "to", "tea", "ted", "ten", "i", "in", "inn"))


if __name__ == "__main__":
    test()
