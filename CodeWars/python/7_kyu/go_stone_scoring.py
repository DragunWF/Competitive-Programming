# https://www.codewars.com/kata/5fdb2ef8656423001c00e648/train/python

def determine_winner(board):
    black_score, white_score = 0, 0
    for row in board:
        for cell in row:
            if cell == "W":
                white_score += 1
            elif cell == "B":
                black_score += 1
    if black_score == white_score:
        return ("T", black_score)
    return ("W", white_score) if white_score > black_score else ("B", black_score)
