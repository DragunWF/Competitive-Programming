# https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

class List:
    def remove_(self, integer_list, values_list):
        return [n for n in integer_list if not n in values_list]