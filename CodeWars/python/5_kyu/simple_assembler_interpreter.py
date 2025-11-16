# https://www.codewars.com/kata/58e24788e24ddee28e000053

def simple_assembler(program: list[str]) -> dict:
    output = {}
    i = 0
    while i < len(program):
        line = program[i]
        tokens = line.split(" ")
        command = tokens[0]
        variable = tokens[1]
        if command == "mov":
            value = extract_token_value(tokens[2], output)
            output[variable] = value
        elif command == "inc":
            output[variable] += 1
        elif command == "dec":
            output[variable] -= 1
        elif command == "jnz":
            variable_value = extract_token_value(variable, output)
            steps = extract_token_value(tokens[2], output)
            if variable_value != 0:
                i += steps
                continue
        i += 1
    return output


def extract_token_value(token: str, output: dict) -> int:
    if token.isdigit() or token.startswith("-"):
        return int(token)
    return output[token]


def test() -> None:
    # Expected: { "a": 1 }
    print(simple_assembler(
        ["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"])
    )
    code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
    # Expected: {'a': 409600, 'c': 409600, 'b': 409600}
    print(simple_assembler(code.splitlines()))


if __name__ == "__main__":
    test()
