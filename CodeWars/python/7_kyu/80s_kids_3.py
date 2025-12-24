# https://www.codewars.com/kata/5662292ee7e2da24e900012f

from collections import Counter


def get_socks(name: str, socks: list[str]) -> str:
    if not socks:
        return []

    if name == "Punky":
        unique_socks = list(set(socks))
        if len(unique_socks) == 1:
            return []
        return [unique_socks[0], unique_socks[1]]
    elif name == "Henry":
        sock_counter = Counter(socks)
        for sock in sock_counter:
            if sock_counter[sock] >= 2:
                return [sock, sock]

    return []


def test() -> None:
    # Expected: ['red', 'blue']
    print(get_socks('Punky', ['red', 'blue', 'blue', 'green']))
    # Expected: ['blue', 'blue']
    print(get_socks('Henry', ['red', 'blue', 'blue', 'green']))


if __name__ == "__main__":
    test()
