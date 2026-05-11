# https://www.codewars.com/kata/59126992f9f87fd31600009b/train/python

def whose_move(last_player: str, win: bool) -> str:
    if win:
        return last_player
    return "white" if last_player == "black" else "black"
