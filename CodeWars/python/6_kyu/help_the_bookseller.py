# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

def stock_list(list_of_art: list[str], list_of_cat: list[str]):
    if not list_of_art:
        return ""
    stocks = {}
    for code in list_of_cat:
        stocks[code] = 0
    for item in list_of_art:
        values = item.split(" ")
        book, sell_value = values[0][0], int(values[1])
        if book in list_of_cat:
            stocks[book] += sell_value
    output = []
    for key in stocks:
        output.append(f"({key} : {stocks[key]})")
    return " - ".join(output)
