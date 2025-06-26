# https://www.codewars.com/kata/551614eb77dd9ee37100003e/train/python


class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        if hero[0] == "B" or hero[2] == "t":
            return f"Batman: {quotes[0]}"
        if hero[0] == "R" or hero[2] == "b":
            return f"Robin: {quotes[1]}"
        if hero[0] == "J" or hero[2] == "k":
            return f"Joker: {quotes[2]}"
