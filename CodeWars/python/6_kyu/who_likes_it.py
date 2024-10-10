# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    output, ppl_cnt = "", len(names)
    if not names:
        return "no one likes this"
    if ppl_cnt <= 2:
        return f"{names[0]} likes this" if ppl_cnt == 1 else f"{names[0]} and {names[1]} like this"
    for name in names:
        if name != names[-2 if ppl_cnt == 3 else 1]:
            output += f"{name}, "
        else:
            if ppl_cnt > 3:
                entities = ppl_cnt - 2
                output += f"{names[1]} and {entities} others like this"
            else:
                output += f"{names[-2]} and {names[-1]} like this"
            return output
