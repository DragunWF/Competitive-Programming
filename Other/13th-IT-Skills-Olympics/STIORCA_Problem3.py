from itertools import product

def solve() -> None:
    stringnumber = input("stringnumber = ")
    target = int(input("target = "))
    operator_count = len(stringnumber) - 1
    placeholder = "_".join([*stringnumber])
    operators = sorted(list(product("+-*", repeat=operator_count)))
    operator_index = 0
    print("Possible expressions:")
    for i in range(len(operators)):
        expression = ""
        for char in placeholder:
            if char == "_":
                expression += operators[i][operator_index]
                operator_index += 1
            else:
                expression += char
        if eval(expression) == target:
            print(expression)
        operator_index = 0


if __name__ == "__main__":
    solve()