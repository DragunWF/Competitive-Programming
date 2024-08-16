# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students: list[Student]) -> str:
    richest_student = students[0]
    if len(students) == 1:
        return richest_student.name
    max_money = get_money(richest_student)
    same_money = 1
    for i in range(1, len(students)):
        money = get_money(students[i])
        if money == max_money:
            same_money += 1
        if money > max_money:
            max_money = money
            richest_student = students[i]
    return richest_student.name if same_money != len(students) else "all"


def get_money(student: Student):
    return student.fives * 5 + student.tens * 10 + student.twenties * 20


def test():
    # Not part of the solution, just testing
    phil = Student("Phil", 2, 2, 1)
    cam = Student("Cameron", 2, 2, 0)
    geoff = Student("Geoff", 0, 3, 0)
    print(most_money([phil, cam, geoff]))
    print(most_money([cam, geoff]))


if __name__ == "__main__":
    test()
