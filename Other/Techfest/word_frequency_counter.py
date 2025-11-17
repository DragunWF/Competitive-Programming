from collections import Counter


def word_frequency(s):
    return Counter(s.split(" "))


if __name__ == '__main__':
    s = input().strip()
    freq = word_frequency(s)
    for word in sorted(freq):
        print(word, freq[word])
