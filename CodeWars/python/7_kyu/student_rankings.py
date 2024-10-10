# https://www.codewars.com/kata/6064c4fe71f8920036610b4b

def post_grades(data: list[str]) -> list[tuple[str, float]]:
    students = []
    for student in data:
        attributes = student.split(" - ")
        grades = [float(n) for n in attributes[2].split(" ")]
        students.append((attributes[0], sum(grades) / len(grades)))
    return sorted(students, key=lambda x: x[1], reverse=True)


def test() -> None:
    # Not part of the solution, just testing
    print(post_grades([
        'S01 - Student Name A - 95 98.4 92.15',
        'S02 - Student Name B - 100 96.4 90',
        'S03 - Student Name C - 84.2 90.5 92.8',
        'S04 - Student Name D - 80 96.4 88.4'
    ]))
    print(post_grades(['1001 - Joonghyuk Yoo - 95 98.4 92.15', '1002 - Dokja Kim - 100 96.4 90',
          '1003 - Boyoung Park - 84.2 90.5 92.8', '1004 - Shijin Yoo - 80 96.4 88.4']))


if __name__ == "__main__":
    test()
