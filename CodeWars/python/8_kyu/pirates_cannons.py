# https://www.codewars.com/kata/5748a883eb737cab000022a6

def cannons_ready(gunners):
    for member in gunners:
        if gunners[member] == "nay":
            return "Shiver me timbers!"
    return "Fire!"
