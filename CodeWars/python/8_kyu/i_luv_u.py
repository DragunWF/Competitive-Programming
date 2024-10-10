# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296

def how_much_i_love_you(nb_petals):
    sentence = ("I love you", "a little", "a lot",
                "passionately", "madly", "not at all")
    return sentence[nb_petals - 1 if nb_petals < 6 else nb_petals % 6 - 1]
