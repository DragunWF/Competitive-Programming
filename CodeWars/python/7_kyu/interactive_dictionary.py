# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python

class Dictionary():
    def __init__(self):
        self.words = {}

    def newentry(self, word, definition):
        self.words[word] = definition

    def look(self, key):
        return self.words[key] if key in self.words else f"Can't find entry for {key}"
