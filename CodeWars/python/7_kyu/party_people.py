# https://www.codewars.com/kata/65013fc50038a68939098dcf

def party_people(people: list[int]) -> list:
    people.sort(reverse=True)
    head_count = len(people)
    for person in people:
        if head_count < person:
            head_count -= 1
    return head_count


def test() -> None:
    print(party_people([4, 5, 4, 1]))
    print(party_people([2, 1, 2, 0]))


if __name__ == "__main__":
    test()
