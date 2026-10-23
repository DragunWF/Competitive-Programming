# https://www.codewars.com/kata/6ad649de715eb5f5359a7e62/train/python

def battery_bars(percent: int) -> str:
    bars = percent // 20
    return f"[{bars * '#'}{(5 - bars) * '.'}]"