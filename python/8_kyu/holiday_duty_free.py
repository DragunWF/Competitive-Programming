# https://www.codewars.com/kata/57e92e91b63b6cbac20001e5/train/python

def duty_free(price, discount, holiday_cost):
    return (holiday_cost / (price * discount / 100)).__floor__()
