import sys


def solve() -> None:
    infix_expression = input("Infix Expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print(f"Infix: {infix_expression}\nPostfix: {postfix_expression}")


def infix_to_postfix(infix: str) -> str:
    while "(" in infix or ")" in infix:
        infix = infix.replace("(", "")
        infix = infix.replace(")", "")

    tokens = infix.split(" ")
    OPERATORS = "+-*/"

    stack = []
    postfix = []
    for token in tokens:
        if token == " ":
            continue
        if token in OPERATORS:
            if stack:
                postfix.append(stack.pop())
            stack.append(token)
        elif token.isdigit():
            postfix.append(token)

    while stack:
        postfix.append(stack.pop())

    return " ".join(postfix)


if __name__ == "__main__":
    solve()