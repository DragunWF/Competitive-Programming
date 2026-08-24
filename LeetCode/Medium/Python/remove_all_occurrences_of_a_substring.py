# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        output = s
        while part in output:
            output = output.replace(part, "", 1)
        return output


def test() -> None:
    test_cases = [
        {"s": "aabababa", "part": "aba", "expected": "ba"},
        {"s": "daabcbaabcbc", "part": "abc", "expected": "dab"}
    ]
    solution = Solution()

    print()
    for i, item in enumerate(test_cases):
        print(f"Test Case #{i + 1}: s: {item['s']}, part: {item['part']}")
        result = solution.removeOccurrences(item["s"], item["part"])
        if result != item["expected"]:
            print(
                f"===> Expected '{item['expected']}' but got '{result}' instead ❌ (Failed)"
            )
        else:
            print(f"===> Got '{result}' ✅ (Passed)")
        print()


if __name__ == "__main__":
    test()
