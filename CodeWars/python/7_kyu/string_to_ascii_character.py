# https://www.codewars.com/kata/5abbb33396194245d5000161


solution=lambda s:chr(sum(map(ord,s.upper()))//len(s))

def test() -> None:
    # Expected: L
    print(solution(
        "iamareallyreallylongstringthatiscompletelyworthlessandisheretostophardcoders"))


if __name__ == "__main__":
    test()
