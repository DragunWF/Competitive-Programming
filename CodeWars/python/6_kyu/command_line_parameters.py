# https://www.codewars.com/kata/53689951c8a5ca91ac000566/train/ruby

def args_to_string(args: list) -> str:
    output = []
    for item in args:
        if type(item) == list:
            if len(item) == 2:
                prefix = "-" if len(item[0]) == 1 else "--"
                output.append(f"{prefix}{item[0]} {item[1]}")
            else:
                output.append(item[0])
        else:
            output.append(item)
    return " ".join(output)


def test() -> None:
    # Expected: "foo --bar baz qux"
    print(args_to_string([["foo"], ["bar", "baz"], "qux"]))


if __name__ == "__main__":
    test()
