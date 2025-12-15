# https://www.codewars.com/kata/56ae72854d005c7447000023/train/python

def create_template(template: str):
    def str_formatter(**kwargs):
        sentence = template
        words = sentence.split(" ")
        output = []
        for word in words:
            if word.startswith("{{") and word.endswith("}}"):
                word = word.replace("{{", "")
                word = word.replace("}}", "")
                output.append(kwargs[word] if word in kwargs else "")
            else:
                output.append(word)
        return " ".join(output)
    return str_formatter


def test() -> None:
    template = create_template("{{name}} likes {{animalType}}")
    print(template(name="John", animalType="dogs"))  # John likes dogs


if __name__ == "__main__":
    test()
