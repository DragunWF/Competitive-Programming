# https://www.codewars.com/kata/57a386117cb1f31890000039/train/python

def parse_float(string: str | list[str]) -> float:
    try:
        if type(string) is str:
            return float(string)
        return [float(n) for n in string]
    except ValueError:
        return None
