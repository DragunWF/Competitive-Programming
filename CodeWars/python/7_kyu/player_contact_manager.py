# https://www.codewars.com/kata/5b203de891c7469b520000b4/python

def player_manager(players: str) -> list[dict]:
    if not type(players) is str:
        return []
    output = []
    info = players.split(", ")
    current_player = {}
    for i, value, in enumerate(info):
        nth = i + 1
        if nth % 2 == 0:
            current_player["contact"] = int(value)
        else:
            current_player["player"] = value
        if "contact" in current_player and "player" in current_player:
            output.append(current_player)
            current_player = {}
    return output


def test() -> None:
    print(player_manager("John Doe, 8167238327, Jane Doe, 8163723827"))


if __name__ == "__main__":
    test()
