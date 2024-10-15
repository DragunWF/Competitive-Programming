# https://www.codewars.com/kata/514a677421607afc99000002/train/python

def itemgetter(item):
    return item['name']


def get_names(data):
    return list(map(itemgetter, data))
