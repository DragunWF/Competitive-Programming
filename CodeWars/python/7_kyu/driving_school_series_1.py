# https://www.codewars.com/kata/58999425006ee3f97c00011f/train/python

def passed(arr: list) -> int | str:
    passed_student_scores = [score for score in arr if score <= 18]
    if not passed_student_scores:
        return 'No pass scores registered.'
    return round(sum(passed_student_scores) / len(passed_student_scores))
