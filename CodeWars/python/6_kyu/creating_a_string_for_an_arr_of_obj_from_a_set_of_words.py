# https://www.codewars.com/kata/5877786688976801ad000100/train/python

def words_to_object(s: str) -> str:
    if not s:
        return "[]"
    words = s.split(" ")
    arr = []
    for i in range(0, len(words), 2):
        arr.append({"name": words[i], "id": words[i + 1]})
    output = str(arr)
    output = output.replace("'name':", 'name :')
    output = output.replace("'id':", "id :")
    return output


def test() -> None:
    print(words_to_object("red 1 yellow 2 black 3 white 4"))


if __name__ == "__main__":
    test()
