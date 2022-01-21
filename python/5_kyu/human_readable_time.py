# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    sec, min, hr, = 0, 0, 0
    for i in range(seconds):
        sec += 1
        if (sec % 60) == 0:
            sec = 0
            min += 1
            if (min % 60) == 0:
                min = 0
                hr += 1 if hr < 99 else 0
    sec = f"0{sec}" if not sec > 9 else sec
    min = f"0{min}" if not min > 9 else min
    hr = f"0{hr}" if not hr > 9 else hr
    return f"{hr}:{min}:{sec}"
