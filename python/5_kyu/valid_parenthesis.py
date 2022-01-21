# https://www.codewars.com/kata/52774a314c2333f0a7000688
# My Cringe Code lol

def valid_parentheses(string):
    values, index, cog = {}, 0, False
    if string.count("(") or string.count(")"):
        try:
            if string.startswith(")") or (string.count("(") % string.count(")")) >= 1:
                return False
        except ZeroDivisionError:
            return False
        for ltr in string:
            if ltr == "(":
                cog += 1
                if not values:
                    values[ltr] = index
                else:
                    values[f"{ltr}-{index}"] = index
            elif ltr == ")":
                for pnt in values:
                    if values[pnt] - index == 0:
                        del values[pnt]
                        cog -= 1
                        break
                else:
                    return False
            if values:
                for pnt in values:
                    values[pnt] += 1
            index += 1
    return True if cog == 0 else False
