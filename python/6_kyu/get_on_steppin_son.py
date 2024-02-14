# https://www.codewars.com/kata/55e00266d494ce5155000032/train/python

def word_step(s: str):
    words = s.split(" ")
    output = []
    matrix_row_len = len(words[0])
    for i in range(1, len(words)):
        if i % 2 == 0:
            matrix_row_len += len(words[i]) - 1

    stop_index = 0
    for i, word in enumerate(words):
        first_half = " " * stop_index
        if i % 2 == 0:
            output.append([*first_half, *word, *
                           (" " * (matrix_row_len - (stop_index + len(word))))])
            stop_index += len(word) - 1
        else:
            second_half = " " * (matrix_row_len - (stop_index + 1))
            for j in range(1, len(word) - 1):
                output.append([*first_half, word[j], *second_half])
            if i + 1 == len(words):
                output.append([*first_half, word[-1], *second_half])
    return output


# Test code
# print(word_step("HELLO OIL"))
output = word_step('SNAKES SHOE EFFORT TRUMP POTATO')
print([len(item) for item in output])
print(output)

[['S', 'N', 'A', 'K', 'E', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'E', 'F', 'F', 'O', 'R', 'T', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'O', 'T', 'A', 'T', 'O']]

[['S', 'N', 'A', 'K', 'E', 'S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'E', 'F', 'F', 'O', 'R', 'T', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'O', 'T', 'A', 'T', 'O']]
