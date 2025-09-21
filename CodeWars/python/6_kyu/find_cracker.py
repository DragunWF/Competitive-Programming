# https://www.codewars.com/kata/59f70440bee845599c000085/train/python

def find_hack(arr: list) -> list[str]:
    letter_scores = {"A": 30, "B": 20, "C": 10, "D": 5}
    hackers = []
    for item in arr:
        name: str = item[0]
        score: int = item[1]
        grades: list[str] = item[2]

        calculated_score = 0
        high_grade_count = 0  # B and above is a high grade
        for grade in grades:
            if not grade in letter_scores:
                continue
            calculated_score += letter_scores[grade]
            if grade == "B" or grade == "A":
                high_grade_count += 1
        if len(grades) >= 5 and high_grade_count == len(grades):
            calculated_score += 20
        if calculated_score > 200:
            calculated_score = 200

        if calculated_score != score:
            hackers.append(name)

    return hackers


def test() -> None:
    array1 = [
        ["name1", 445, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 110, ["B", "A", "A", "A"]],
        ["name3", 200, ["B", "A", "A", "C"]],
        ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]]
    ]
    print(find_hack(array1))  # name1, name3

    array2 = [
        ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
        ["name2", 120, ["B", "A", "A", "A"]],
        ["name3", 160, ["B", "A", "A", "A", "A"]],
        ["name4", 140, ["B", "A", "A", "C", "A"]]
    ]
    print(find_hack(array2))  # name2, name4


if __name__ == "__main__":
    test()
