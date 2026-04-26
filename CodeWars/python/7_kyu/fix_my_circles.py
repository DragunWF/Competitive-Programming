# https://www.codewars.com/kata/68332539defbf760434582d1/train/python

def circle_mender(content: str) -> str:
    lines = content.split("\n")
    output_lines = []
    for line in lines:
        start, end = None, None
        for i, char in enumerate(line):
            if char == "#":
                start = i
                break
        if not start is None:
            for i in range(len(line) - 1, -1, -1):
                if line[i] == "#":
                    end = i
                    break

        if not start is None:
            filled_circle_line = []
            for i, char in enumerate(line):
                filled_circle_line.append("#" if start <= i <= end else char)
            output_lines.append("".join(filled_circle_line))
        else:
            output_lines.append(line)
    return "\n".join(output_lines)
