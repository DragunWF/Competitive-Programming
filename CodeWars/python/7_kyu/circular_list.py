# https://www.codewars.com/kata/5b2e60742ae7543f9d00005d/train/python

class CircularList():
    def __init__(self, *args):
        if not args:
            raise Exception()
        self.data = args
        self.current_index = -1

    def next(self):
        self.current_index += 1
        if self.current_index >= len(self.data):
            self.current_index = 0
        return self.data[self.current_index]

    def prev(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.data) - 1
        return self.data[self.current_index]
