# https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/python

def sentence(data: list[dict]) -> str:
    return " ".join([list(item.values())[0] for item in sorted(data, key=lambda dict: int(list(dict.keys())[0]))])


def test():
    # Not part of the solution, just testing
    print(sentence([
        {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
    ]))


if __name__ == '__main__':
    test()
