def solve() -> None:
    judge_scores = []
    print("-" * 25)
    print("Enter judge's scores:")
    for i in range(8):
        num = input_score(f"Judge {i + 1} => ")
        judge_scores.append(num)
    print("-" * 25)

    judge_scores.remove(get_max(judge_scores))
    judge_scores.remove(get_min(judge_scores))

    print("-" * 25)
    print("Judges Final Score:")
    print(" ".join([str(score) for score in judge_scores]))

    total_score = format(get_total_score(judge_scores), ".2f")
    print(f"TOTAL SCORE: {total_score}")


def input_score(input_str: str) -> float:
    try:
        score = float(input(input_str))
        if not (1 <= score <= 10):
            print("Score must be between 1.0 to 10.0 points!")
            return input_score(input_str)
        return score
    except ValueError:
        print("Score must be numeric value!")
        return input_score(input_str)


def get_min(scores: list[float]) -> float:
    min_float = scores[0]
    for i in range(1, len(scores)):
        if scores[i] < min_float:
            min_float = scores[i]
    return min_float


def get_max(scores: list[float]) -> float:
    max_float = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_float:
            max_float = scores[i]
    return max_float


def get_total_score(scores: list[float]) -> float:
    total = 0
    for score in scores:
        total += score
    return total


if __name__ == "__main__":
    solve()