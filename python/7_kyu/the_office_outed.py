# https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/train/python

def outed(meet: dict[str, int], boss: str) -> str:
    total_ratings = 0
    for name in meet:
        total_ratings += meet[name] if name != boss else meet[name] * 2
    return "Get Out Now!" if total_ratings / len(meet) <= 5 else "Nice Work Champ!"
