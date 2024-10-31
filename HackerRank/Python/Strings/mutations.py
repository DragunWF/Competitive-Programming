# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    char_arr = [*string]
    char_arr[position] = character
    return "".join(char_arr)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
