# https://www.codewars.com/kata/5b36137991c74600f200001b/train/python

def kill_monsters(health, monsters, damage):
    hits = 0
    while True:
        monsters -= 3
        if monsters <= 0:
            break
        hits += 1
    if hits < 0:
        hits = 0
    damage = hits * damage
    health = health - damage
    return ("hero died" if health <= 0 else
            f"hits: {hits}, damage: {damage}, health: {health}")


print(kill_monsters(50, 7, 10))  # "hits: 2, damage: 20, health: 30"
print(kill_monsters(100, 3, 33))  # "hits: 0, damage: 0, health: 100"
print(kill_monsters(30, 4, 50))  # "hero died"
