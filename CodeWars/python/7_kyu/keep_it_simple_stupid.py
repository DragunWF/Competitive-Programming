# https://www.codewars.com/kata/57eeb8cc5f79f6465a0015c1/train/python

def is_kiss(words: str) -> str:
    word_list = words.split(" ")
    word_count = len(word_list)
    for word in word_list:
        if len(word) > word_count:
            return "Keep It Simple Stupid"
    return "Good work Joe!"


def test() -> None:
    # Expected: Good work Joe!
    print(is_kiss("Joe had a bad day"))
    # Expected: Keep It Simple Stupid
    print(is_kiss("Joe listened to the noises and there were some onamonapias"))


if __name__ == "__main__":
    test()
