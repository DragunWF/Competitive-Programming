from math import floor
# https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_duration(seconds):
    if not seconds:
        return "now"
    sec, hr, mn = seconds, floor(seconds / 3600), floor(seconds / 60)
    days, years = floor(hr / 24), floor(hr / 8760)
    sec, mn, hr, days = sec - (mn * 60), mn - \
        (hr * 60), hr - (days * 24), days - (years * 365)
    word_s = "seconds" if sec > 1 else "second"
    word_m = "minutes" if mn > 1 else "minute"
    word_h = "hours" if hr > 1 else "hour"
    word_d = "days" if days > 1 else "day"
    word_y = "years" if years > 1 else "year"
    sc, mt, hu, ds, yr, index = sec, mn, hr, days, years, 0
    sec, mn, hr = f"{sec} {word_s}", f"{mn} {word_m}", f"{hr} {word_h}"
    days, years = f"{days} {word_d}", f"{years} {word_y}"
    values, wrd, snt = (yr, ds, hu, mt, sc), (years, days, hr, mn, sec), []
    for value in values:
        if value:
            snt.append(wrd[index])
        index += 1
    if len(snt) > 2:
        output = ""
        for cog in snt:
            if cog == snt[-2]:
                break
            output += f"{cog}, "
        return f"{output.rstrip()} {snt[-2]} and {snt[-1]}"
    return f"{snt[0]} and {snt[1]}" if len(snt) > 1 else f"{snt[0]}"
