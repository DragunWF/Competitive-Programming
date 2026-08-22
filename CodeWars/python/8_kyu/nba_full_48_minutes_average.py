# https://www.codewars.com/kata/587c2d08bb65b5e8040004fd/train/python

# I actually just got home from AWS Community Day Philippines 2026 when
# I did this problem. I just went with quick one primarily because I felt
# too tired when I got home and just wanted to sleep but either way I didn't
# want to break my habit so I just solved this quick problem instead hehe :)

def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return round(ppg / mpg * 48, 1)
