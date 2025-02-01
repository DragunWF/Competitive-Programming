# https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python

def capital(capitals: list[dict]):
    output = []
    for capital in capitals:
        place = capital["state"] if "state" in capital else capital["country"]
        output.append(f"The capital of {place} is {capital['capital']}")
    return output
