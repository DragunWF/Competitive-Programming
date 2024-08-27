# https://www.codewars.com/kata/57158fb92ad763bb180004e7/train/python

def rain_amount(mm):
    if mm < 40:
        return f"You need to give your plant {40 - mm}mm of water"
    return "Your plant has had more than enough water for today!"
