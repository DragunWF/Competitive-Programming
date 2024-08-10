# https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python

def validate_hello(greetings):
    hello = {
        "hello": "english",
        "ciao": "italian",
        "salut": "french",
        "hallo": "german",
        "hola": "spanish",
        "ahoj": "czech republic",
        "czesc": "polish"
    }
    for word in hello:
        if word in greetings.lower():
            return True
    return False
