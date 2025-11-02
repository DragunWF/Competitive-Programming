# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python

def josephus(items: list, k: int) -> list:
    survivors = [*items]
    permutation = []
    count = 1
    while survivors:
        surviving_batch = []
        for survivor in survivors:
            if count % k == 0:
                permutation.append(survivor)
            else:
                surviving_batch.append(survivor)
            count += 1
        survivors = surviving_batch
    return permutation


def test() -> None:
    # Expected: [3,6,2,7,5,1,4]
    print(josephus([1, 2, 3, 4, 5, 6, 7], 3))


if __name__ == "__main__":
    test()
