# https://www.codewars.com/kata/5837fd7d44ff282acd000157/train/python

from datetime import datetime


def count_days(target: datetime):
    today = datetime.now()
    date_today = today.date()
    target_date = target.date()

    if date_today == target_date:
        return "Today is the day!"
    elif target_date < date_today:
        return "The day is in the past!"
    return f"{round(((target - today).total_seconds() / 3600) / 24)} days"
