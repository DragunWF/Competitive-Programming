# https://www.codewars.com/kata/58b28e5830473070e5000007/train/python

def frame(score_data: str) -> list[int, int]:
    output = [0, 0]
    scores = score_data.split(";")
    for result in scores:
        points = result.split("-")
        first, second = formalize_score(points[0]), formalize_score(points[1])
        output[int(first < second)] += 1
    return output


def formalize_score(score: str) -> int:
    return int(score.split("(")[0]) if "(" in score else int(score)


def test():
    # Not part of the solution, just testing
    test_case = "24-79(72); 16-101(53); 86(58)-27; 31-90(74); 0-115(115); 67-40; 61-21; 81(55)-23; 51-14; 124(56,68)-4; 67-12; 108(85)-15; 1-117(117); 1-92(92); 130(112)-0; 1-106(53); 59-39"
    print(frame(test_case))


if __name__ == '__main__':
    test()
