# https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

if __name__ == '__main__':
    k = int(input())
    rooms = Counter(input().split(" "))
    for room in rooms:
        if rooms[room] != k:
            print(room)
            break
