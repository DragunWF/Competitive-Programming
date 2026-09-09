# https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python

from datetime import datetime


def is_today(date: datetime) -> bool:
    return str(date).split(" ")[0] == str(datetime.today()).split(" ")[0]
